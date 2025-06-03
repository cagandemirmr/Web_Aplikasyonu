from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    desciption =Column(String)
    priority =Column(Integer)
    complete = Column(Boolean,default=False)
    owner_id = Column(Integer,ForeignKey('users.id')) #kime ait olduğunu belirtmek için

#Authentication için sınıf oluştururuz.Bir neviburada database oluşturuyoruz
# Class ta yaptıklarımızın Fastapi ye yansıması için migration işlemi yapmamız gerekir.
#Eğer migration işlemiyle uğraşmak istemiyorsak refactor yaparız yani reset çekeriz.

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String) #Parolalar hiçbir zaman açık metin olarak tutulmamalıdır.
    is_active = Column(Boolean,default=True) #Bir kaç uygulamada böyle işlemlerde var.
    role = Column(String)
    phone_number =Column(String)

