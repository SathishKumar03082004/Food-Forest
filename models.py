from sqlalchemy import Column, String, Integer,Date
from sqlalchemy.orm import sessionmaker
from database import base,db_engine


class SignUp(base):
    __tablename__="login"
    id = Column(Integer, primary_key=True, index=True)
    username=Column(String(20),unique=True)
    password=Column(String(10))
    #status=Column(String(20))

# class New(base):
#     __tablename__="user"
#     id=Column(Integer,primary_key=True,index=True)
#     fullname=Column(String(20))
#     username=Column(String(20))
#     email=Column(String(20))
#     password=Column(String(20))
#     status=Column(String(10))

base.metadata.create_all(bind=db_engine)