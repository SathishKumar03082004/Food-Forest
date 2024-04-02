from sqlalchemy import Column, String, Integer,Date
from sqlalchemy.orm import sessionmaker
from database import base,db_engine


class SignUp(base):
    __tablename__="login"
    id = Column(Integer, primary_key=True, index=True)
    username=Column(String(20),unique=True)
    password=Column(String(10))


base.metadata.create_all(bind=db_engine)