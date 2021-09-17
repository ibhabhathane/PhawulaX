import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# from sql import db

# USO OBRIGATÓRIO 
DATABASE_URL = "mongodb+srv://Userbot8778:sasasaSa77@cluster0.eqbcq.mongodb.net/dbtest?retryWrites=true&w=majority" # os.environ.get("DATABASE_URL")

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
