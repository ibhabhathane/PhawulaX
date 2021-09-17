import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# USO OBRIGATÓRIO 
DATABASE_URL = "postgresql://postgres:Asc2shJJ2WVQE9ChtXzT@containers-us-west-9.railway.app:6210/railway"# "sqlite://"# os.environ.get("DATABASE_URL")

def start() -> scoped_session:
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))

try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print("DATABASE_URL não foi configurada.")
    print(str(e))