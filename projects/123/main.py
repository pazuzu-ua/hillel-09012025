from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


DATABASE_URL = "sqlite:///./cats.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    breed = Column(String)
    age = Column(Integer)
    owner = Column(String)


Base.metadata.create_all(bind=engine)


class CatCreate(BaseModel):
    name: str
    breed: str
    age: int
    owner: str

class CatResponse(BaseModel):
    id: int
    name: str
    breed: str
    age: int
    owner: str


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/cats/", response_model=CatResponse)
def create_cat(cat: CatCreate, db: Session = next(get_db())):
    db_cat = Cat(**cat.dict())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


@app.get("/cats/{cat_id}", response_model=CatResponse)
def read_cat(cat_id: int, db: Session = next(get_db())):
    cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return cat


@app.get("/cats/", response_model=list[CatResponse])
def read_cats(skip: int = 0, limit: int = 10, db: Session = next(get_db())):
    cats = db.query(Cat).offset(skip).limit(limit).all()
    return cats