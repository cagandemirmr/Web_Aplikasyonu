from fastapi import FastAPI, Request
from .models import Base, Todo
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse #Nokta koyarak server a biraz daha ahanda burada demek istiyoruz.
from starlette import status
from .database import engine, SessionLocal
from typing import Annotated
from .routers.auth import router as auth_router
from .routers.todo import router as todo_router
import os #Server ın statik dosyaları görmesi için bu işlemi yaparım


app = FastAPI()

script_dir = os.path.dirname(__file__) #Bilgisayarda hangi dosyadaysa path te de aynı dosyada olsun.
st_abs_path = os.path.join(script_dir,"static") #Statik ile mevcut konumu birleştir deriz.


app.mount("/static",StaticFiles(directory="static"),name="static") #Statik dosyaların bağlanması için bu işlemi yaparız.


@app.get("/")
def read_root(request:Request):
    return RedirectResponse(url="/todo/todo-page",status_code=status.HTTP_302_FOUND) #Kullanıcının default ta ana sayfayı görmesi sağlanır.




app.include_router(auth_router)
app.include_router(todo_router)

Base.metadata.create_all(bind=engine)






