from fastapi import APIRouter,Depends, HTTPException, Request
from pydantic import BaseModel
from starlette import status
from ..models import User
from passlib.context import CryptContext #Bu işlemi hashlemek için kullanırız.
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer #Hackerın sisteme sızmasını engellemek için bu işlemi yaparız.
from ..database import SessionLocal #Models dosyasına erişebilmek için iki nokta konulması gerekiyor.
from sqlalchemy.orm import Session
from jose import jwt,JWTError
from datetime import timedelta,datetime, timezone
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

templates = Jinja2Templates(directory="app/templates")

SECRET_KEY = "47k5bocazjgh0r8hje8bvrrn0a71wf7q" #Random.org dan 32 karakterli string yazdırılabilir.
ALGORITHYM = "HS256" #Genelde piyasada en çok tercih edilen algoritmadır.



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
outh2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/login")

#Burada biraz daha biz veri tipinin cinsini belirtiyoruz.
class CreateUserRequest(BaseModel):
    user_name : str
    email : str
    first_name : str
    last_name : str
    password : str
    role : str
    phone_number : str

class Token(BaseModel):
    access_token : str
    token_type : str




def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    payload = {'sub':username,'id':user_id,'role':role}
    expires = datetime.now(timezone.utc) + expires_delta #Şu andan belirlediğim ekstra zamana kadar iptal edilme işlemidir
    payload.update({'exp':expires})
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHYM)


def authenticate_user(username: str,password: str,db):
    user = db.query(User).filter(User.username == username).first() #Sorgulama işlemini yaarım
    if not user:
        return False
    if not bcrypt_context.verify(password,user.hashed_password):
        return False
    return user

async def get_current_user(token: Annotated[str,Depends(outh2_bearer)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHYM)
        username = payload.get('sub') #sub jwt de kullanıcı adına denk gelmektedir
        user_id = payload.get('id')
        user_role = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="username or user ID  invalid")
        return {'username':username,'id':user_id,'role':user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@router.get("/login-page")
def render_login_page(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

@router.get("/register-page")
def render_register_page(request:Request):
    return templates.TemplateResponse("register.html",{"request":request})



@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(db : db_dependency,create_user_request:CreateUserRequest):
    user = User(
        username = create_user_request.user_name ,
        email = create_user_request.email,
        first_name =create_user_request.first_name,
        last_name = create_user_request.last_name,
        role = create_user_request.role,
        is_active = True,
        hashed_password = bcrypt_context.hash(create_user_request.password) ,#Script yapmak için kullanırız.
        phone_number = create_user_request.phone_number
    )
    db.add(user) #Insert işlemi yaparız
    db.commit() #Kayıt işlemini tamamlarız.

@router.post("/token",response_model= Token) #Kullanıcının adını almak için bu sistemi yürütürüz.
async  def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:db_dependency):
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Incorrect username or password')
    token = create_access_token(user.username,user.id,user.role,timedelta(minutes=60))
    return {"access_token":token,"token_type":"bearer"}