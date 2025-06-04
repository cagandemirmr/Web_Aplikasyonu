# Web_Aplikasyonu
Dersin İçeriği:
https://www.youtube.com/watch?time_continue=8&v=k-R6OS-R9mw&embeds_referring_euri=https%3A%2F%2Fegitim.yapayzekaveteknolojiakademisi.com%2F

### Ders Öncesi Hazırlık:
https://www.youtube.com/watch?v=2Yeag12m8N8&t=159s

### Sanal Ortam: 
https://www.youtube.com/watch?time_continue=1&v=88snF6QmayE&embeds_referring_euri=https%3A%2F%2Fegitim.yapayzekaveteknolojiakademisi.com%2F

## PYTHON2 201:
Pydantic:https://www.youtube.com/watch?time_continue=13&v=It9YI2-jcgo&embeds_referring_euri=https%3A%2F%2Fegitim.yapayzekaveteknolojiakademisi.com%2F

Pydantic Repo: https://github.com/atilsamancioglu/P26-PydanticExplained/tree/main

Pydantic Neden Çıktı: https://www.youtube.com/watch?v=Xv-1omNk_tk

Pydantic Örneği: https://www.youtube.com/watch?v=BXA4HYToGMg&t=240s

Asenkron Porgramlama nedir:https://www.youtube.com/watch?v=62uiSQ_q-GU&t=50s

Asenkron Repo: https://github.com/atilsamancioglu/P25-AsyncAwaitExplained/tree/main

Asenkron uygulama: [https://www.youtube.com/watch?time_continue=10&v=RXaU-WFqzik&embeds_referring_euri=https%3A%2F%2Fegitim.yapayzekaveteknolojiakademisi.com%2F](https://www.youtube.com/watch?v=RXaU-WFqzik&t=38s)

## FASTAPI

FastApi nedir:https://www.youtube.com/watch?v=dSWNGW0UJIs&t=49s

Api Nedir: https://www.youtube.com/watch?v=VF_npN9Y54k&t=19s


Yapay zeka modellerini web de deploy etmek için kullanacağım sistemler.

![image](https://github.com/user-attachments/assets/9a627675-df07-4410-8fc1-c162287b3779)
API Backend ile web aplikasyonu arasındadır.

FastAPI çalıştırma: https://www.youtube.com/watch?v=la2T9akiMqc&t=2s

FastAPI repo: https://github.com/atilsamancioglu/FastAPICrud/blob/main/main.py

Kodu yazdıktan sonra terminale  uvicorn main:app --reload yazmamız gereklidir. '/' işareti burada ana sayfa demektir.
Eğer uvicorn da hata varsa o zaman pip install uvicorn diyerek yükleme yapabiliriz.
Ya da pip install "fastapi[standard]" diye yükleme işlemi yapılabilir.Sonra fastapi run main.py

HTTP Protokolleri: https://www.youtube.com/watch?v=jiMYHdkT03Q&t=120s

CRUD da yaptığımız şeylerin HTTP de karşılığı:
![image](https://github.com/user-attachments/assets/dba35bb7-3f97-44bc-ade3-d51238843605)

JSON : Javascript object notation = https://www.youtube.com/watch?v=fI_lGLBzyZk&t=27s
Her fonksiyon sözlük gibi bir çıktı vermek zorunda olduğu için bu yöntemi tercih ederiz.

İlk get işlemi:https://www.youtube.com/watch?v=xhlBjHzPXvQ&t=686s
FastAPI de docs uzantısıyla istediğimiz alana gidebiliriz.
![image](https://github.com/user-attachments/assets/6dd2e651-bfeb-4f95-8d93-fe45059031d5)

Path parametreleri: https://www.youtube.com/watch?v=8GrLNsw-wR4&t=529s
Path Çakışmaları: https://www.youtube.com/watch?v=LjCEK6gwht4&t=358s
Path çakışmalarını önlemek için path in içine ayrı bir path ekleriz.
![image](https://github.com/user-attachments/assets/76908641-6175-4c0e-942b-9fab203831f6)

 ``` python #this will work because it has a different path
@app.get("/courses/byid/{course_id}")
async def get_course(course_id: int):
    for course in courses_db:
        if course.get('id') == course_id:
            return course
```



Querry ile filtreleme : https://www.youtube.com/watch?v=PHhf-pTR2go&t=91s
Burada tek yaptığımız cources tan sonra slash işareti koymak ve boş bir liste tanımlamak



``` python @app.get("/courses/")
async def get_category_by_query(category: str):
    courses_to_return = []
    for course in courses_db:
        if course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return  
```


Path ve Querry : https://www.youtube.com/watch?v=40cNR0QYEMc&t=51s


```python @app.get("/courses/byinstructor/")
async def get_courses_by_instructor_path(instructor: str):
    courses_to_return = []
    for course in courses_db:
        if course.get('instructor').casefold() == instructor.casefold():
            courses_to_return.append(course)

    return courses_to_return

@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str, category: str):
    courses_to_return = []
    for course in courses_db:
        if (course.get('instructor').casefold() == course_instructor.casefold()
                and course.get('category').casefold() == category.casefold()):
            courses_to_return.append(course)

    return courses_to_return
```
Post: https://www.youtube.com/watch?v=FkAXb9ZeHJc&t=84s
FastAPI modülüne ek olarak Body modülünü de eklemeliyiz.
Eğer notasyon farkı olur ve hata verirse; Tek tırnağı çift tırnakla değiştiririz.
![image](https://github.com/user-attachments/assets/5e526580-1146-4bd2-a82b-6993069c871a)

```python @app.post("/courses/create_course")
async def create_course(new_course=Body()):
    courses_db.append(new_course)
```

UPDATE ve DELETE: https://www.youtube.com/watch?v=lIsbzurJDT0&t=36s

Sıra önemli olduğu zaman index olarak for loop unu alırız.

```python @app.put("/courses/update_course")
async def update_course(updated_course=Body()):
    for i in range(len(courses_db)):
        if courses_db[i].get('id').casefold() == updated_course.get('id').casefold():
            courses_db[i] = updated_course


@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id: str):
    for i in range(len(courses_db)):
        if courses_db[i].get('id').casefold() == course_id.casefold():
            courses_db.pop(i)
            break
```

## FASTAPI ORTA
HTTPExeption ile status doğrulanmazsa bile bir şekilde çalıştırabiliriz.
Repo = https://www.youtube.com/watch?v=tBGUxNM7H68&t=192s
Field, karakter sayısı gibi kısıtlamalar yapmamızı sağlar.
Model ve Mock DB = https://www.youtube.com/watch?v=O1OnCooK1oE&t=382s

Status Code Seçenekleri = https://www.youtube.com/watch?v=WmVFUAPJZTk&t=302s
![image](https://github.com/user-attachments/assets/ab7c867e-e8de-42f9-9ebd-cce04e3a37a3)
gt = greater than lt = less than anlamına gelmektedir.

```python
@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(course_id: int = Path(gt=0)):
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=404, detail='Course not found')
```
Raise ile eğer kullanıcı bizim ayarlarımızın dışına çıkarsa ne yapmamız gerektiğini buluruz.

Querry işlemi= https://www.youtube.com/watch?v=qGeFsuo_Zb8&t=627s

Pydantic İstekler = https://www.youtube.com/watch?v=RCASp7KplEI&t=152s
Kendi body mizi oluşturmak istememizin nedeni kendi request isteklerimizi belirlemektir. Mesela veri tipi ve karakter sayısını belirlemek gibi.
gte= greater than or equal to lte= less than or equal to anlamını taşır. Model_config diyerek te mevcut json şemasını overwright etmi oluruz.

```python
class CourseRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not required', default=None)
    title: str = Field(min_length=3)
    instructor: str = Field(min_length=3)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)
        model_config = {
        "json_schema_extra": {
            "example": {
                "title": "course title",
                "instructor": "atil samancioglu",
                "rating": 5,
                'published_date': 2027
            }
        }
    }

```
Eğer modeldeki bilgilerin otomatik olarak yazılmasını istiyorsak o zaman model_dump tan istediğimiz değerleri otomatik doldurabiliriz.Ancak id otomatik tamamlamıyorsa o zaman bir python fonksiyonu yazmamız gereklidir.

```python @app.post("/create-course", status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    new_course = Course(**course_request.model_dump())
    courses_db.append(find_course_id(new_course))


def find_course_id(course: Course):
    course.id = 1 if len(courses_db) == 0 else courses_db[-1].id + 1
    return course
```

Update = https://www.youtube.com/watch?v=XmsD4dkzLEg&t=375s
Delete işlemi = https://www.youtube.com/watch?v=oagxrJsDwok&t=381s

## Veri Tabanı İşlemleri
Veri Tabanları = https://www.youtube.com/watch?v=6h_J96ubeog&t=727s
Select işlemi = https://www.youtube.com/watch?v=5sHfs4a2iZ0
Insert işlemleri = https://www.youtube.com/watch?v=5WSdmoKfAG0&t=462s
Guncelleme ve silme = https://www.youtube.com/watch?v=1B-CZ32cMWo&t=468s
```sql
--create table IF NOT EXISTS urunler (id INTEGER PRIMARY KEY,isim varchar,fiyat INTEGER);

--DELETE FROM urunler WHERE id = 7;

UPDATE urunler SET isim = 'Ayakkabı' where id = 1;

SELECT * from urunler;

--INSERT INTO urunler (isim,fiyat) VALUES ('Etek',2200);
```
Gemini Todo App Tanıtım videosu = https://www.youtube.com/watch?v=XTeET9EayJM&t=393s
ToDoGemini App reposu = https://github.com/atilsamancioglu/ToDoGeminiApp/blob/main/main.py
Proje Başlatmak= https://www.youtube.com/watch?v=KXwIipKHjk4&t=293s
cryptography kütüphanesini yüklememizdeki neden kullanıcı şifrelerini şifrelemek.
sqlalchemy, sql ile olan bağlantıyı kurmak için bağlantı kurulabiliyor.
SQL LITE kurmak = https://www.youtube.com/watch?v=uG5Vv4vGnII&t=517s

Veri Tabanı Bağlantı Kodları = https://www.youtube.com/watch?v=Ig56LZFJM6o&t=490s
Normalde sunucunun ayrı bir portta çalışıyor olması gerekliydi.
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./todoai_app.db"
#SQLALCHEMY_DATABASE_URL ="postgresql: //user:password@postgreserver/db

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Bu base modelini mainde kullanacağız
```
Veri tabanı kolonlarına karar vermek = https://www.youtube.com/watch?v=ESmNivS9s7I&t=551s

Veri tabanı Yöneticileri= https://www.youtube.com/watch?v=VOnAXaQBLz8&t=839s
Veri tabanını terminalde görüntülemek için;
```bash
sqlite3 todoai_app.db
```
sonra


````.show
select * from todos

ile tabloyu görüntüleyebiliyoruz.
`````
## Dependency Injection



Dependency Injection nedir = https://www.youtube.com/watch?v=RDkCphYnnFc&t=564s
Repo = https://github.com/atilsamancioglu/FastAPIDependencyInjectionExplained

Annotation = https://www.youtube.com/watch?v=gWfanTFxJAE&t=145s
Fonksiyonun ihtiyaçlarını bir değikene atadı.
Repo = https://github.com/atilsamancioglu/FastAPIDependencyInjectionExplained/blob/main/annotatedexample.py

Verileri Okumak = https://www.youtube.com/watch?v=u4zeq-8HgSg&t=490s

ID ye Göre Filtreleme: https://www.youtube.com/watch?v=uzzKcw0zlxk&t=374s


Post işlemi: https://www.youtube.com/watch?v=leDTzJgGZpI&t=396s
İşlemi otomatikleştirmek için class içine alırız.

```class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
```

Fastapi da işlem girmek için bunu yaparız.
```app.post("/create-todo",status_code=status.HTTP_201_CREATED)
   async def create_todo(db:db_depency,todo_request =TodoRequest)
   todo = Todo(**todo_request.dict())
   db.add(todo)
   db.commit() #Burada değişiklikleri database e yazarız.
```
 Upgrade ve Delete işlemleri =
 ```python @app.put('/update-todo/{todo_id}',status_code=status.HTTP_204_NO_CONTENT)
           ascync def update_todo(db:db_dependency,
                                  todo_request: TodoRequest,
                                  todo_id: int = Path(gt=0)):
               todo = db.querry(Todo).filter(Todo_id == todo_id).first()
               if todo is  None:
                  raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "Todo not found")
               todo.title = todo_request.title
               todo.description = todo_request.description
               todo.priority = todo_request.priority
               todo.complete = todo_request.complete

               db.add(todo)
               db.commit()

           @app.delete("/delete_todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
            async def delete_todo(db:db_dependency,todo_id:int = Path(gt=0)):
                todo = db.querry(Todo).filter(Todo_id == todo_id).first()
                if todo is None:
                    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "Todo not found")
                db.querry(Todo).filter(Todo_id == todo_id).delete()
                db.commit()
```
Update ve Delete = https://www.youtube.com/watch?v=2DBjkq8wRCA
## Router mantığı

Router mantığı = https://www.youtube.com/watch?v=lqpzw1pkV7Q

Router = https://www.youtube.com/watch?v=o6s3I78Hszk&t=2s

Users Tablosu = https://www.youtube.com/watch?v=Dgk2n8L3kII

İlişkisel Tablo incelemesi = https://www.youtube.com/watch?v=tJgj_T0nIzU&t=757s

Parola ve Şİfre İlişkisi : https://www.youtube.com/watch?v=cImgyetQEdk&t=584s

Şifreleme işlemi: https://www.youtube.com/watch?v=Sf6A2YO1Ws0&t=607s

Giriş Yapma Mantığı: https://www.youtube.com/watch?v=AoYU1h-3DPk

JWT: her yeni ziyaretçi için ayrı bir token verilir bu tokenın en son şifrelemesini biz yaparız.

![image](https://github.com/user-attachments/assets/edf8a109-a277-4cb9-ad5c-ad0d58b9681d)


https://www.youtube.com/watch?v=sE_z3TJ9qoI&t=726s

JWT encoding : https://www.youtube.com/watch?v=TvD6Iy-JEE0&t=694s

JWT decoding: https://www.youtube.com/watch?v=k7l3t40CENg

İstek Limitleri: Kilit logosuna tıklandığında authentication vermiş oluruz.Ancak bu işlem tarayıcıda yapılır.
https://www.youtube.com/watch?v=XKjf4Jm_GKM&t=454s

Kullanıcı Filtreleri: https://www.youtube.com/watch?v=ZbH5i5ukitY&t=573s

Güncelleme ve silme: https://www.youtube.com/watch?v=bYr4YnI9Th4&t=629s

# Migration

Veri tabanını hızlıca güncellemek için kullanılır.

alembic init aembic denilirse bu işlemle ilgili dosya açılacaktır. Burada alembic.ini ve env dosyasında değişiklik yaplır.

https://www.youtube.com/watch?v=8weQ9CjZpsI&t=364s

Migration: gerekli işlemleri yaptıktan sonra terminale şunu yazarız: alembic revision -m "phone number added" böylece değişiklikleri işlemiş oluruz.
link: https://www.youtube.com/watch?v=e4C6fmBPmMg&t=972s

# Frontend
Giriş: https://www.youtube.com/watch?v=XjuRl0-RVAs&t=344s

Ön yüz dosyalarının üstünden geçme: https://www.youtube.com/watch?v=843HFL6K3z8&t=441s
template in içerisinde layout projenin genel hatlarıdır.Ve basit bir CS kütüphanesi olan Bootstrap i kullanır.

Ana uygulamayı bağlama: Sonraki aşamalarda auth ve todo py dosyalarını template e bağlarız.
https://www.youtube.com/watch?v=bTWotGlUgQM&t=388s

Register ve login page: https://www.youtube.com/watch?v=b6XktOYTg2M&t=392s
Auth ta login ve register bağlamalarını yaparız.

Cookies: https://www.youtube.com/watch?v=IZRGW65_5wg&t=753s
Tüm sayfaları renderlamak: https://www.youtube.com/watch?v=zWLMmzOiiDw&t=511s

# Gemini
Gemini_API_Key : https://www.youtube.com/watch?v=AXignG8nknA&t=356s

Langchain entegrasyonu : https://www.youtube.com/watch?v=kTzr7sNwDH0&t=475s

Tanım kısmını Gemini a yazdırmak: https://www.youtube.com/watch?v=QWByvNHZu5E

# Docker
Docker: https://www.youtube.com/watch?v=rxrU81dOskQ&t=376s

Relative import and Abs : https://www.youtube.com/watch?v=S6vL5Smy8EA&t=414s

Google Cloud: https://www.youtube.com/watch?v=2icBXgHDZ2Y&t=601s

Docker kurulumu: https://www.youtube.com/watch?v=xhrg8m9su5o&t=525s

Canlıya almak: https://www.youtube.com/watch?v=hRWcnfakDoI&t=309s
