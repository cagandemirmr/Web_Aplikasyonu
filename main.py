from fastapi import FastAPI, Request
from models import Base, Todo
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette import status
from database import engine, SessionLocal
from typing import Annotated
from routers.auth import router as auth_router
from routers.todo import router as todo_router


app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static") #Statik dosyaların bağlanması için bu işlemi yaparız.


@app.get("/")
def read_root(request:Request):
    return RedirectResponse(url="/todo/todo-page",status_code=status.HTTP_302_FOUND) #Kullanıcının default ta ana sayfayı görmesi sağlanır.




app.include_router(auth_router)
app.include_router(todo_router)

Base.metadata.create_all(bind=engine)






