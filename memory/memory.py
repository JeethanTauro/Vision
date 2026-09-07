from sqlmodel import create_engine, SQLModel
from session_model import *
DATABASE_URL = "sqlite:////home/jeethan/Desktop/vision/data/vision_memory.db"


engine  =  create_engine(url=DATABASE_URL, echo=False)

SQLModel.metadata.create_all(engine)

def get_engine():
    return engine

