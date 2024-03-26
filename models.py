from sqlalchemy import Column, String, Integer,Date
from sqlalchemy.orm import sessionmaker
from database import base,db_engine


base.metadata.create_all(bind=db_engine)