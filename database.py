from sqlalchemy import create_engine
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = URL.create(
    'postgresql',
    username='koyeb-adm',
    password='********',
    host='ep-blue-feather-a2fl2yth.eu-central-1.pg.koyeb.app',
    database='Food',
)

db_engine = create_engine(DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

base=declarative_base()
