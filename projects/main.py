from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

# --- База даних ---
DATABASE_URL = "sqlite:///./demonslayer.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# --- SQLAlchemy модель ---
class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    breathing_style = Column(String)
    rank = Column(String)
    is_hashira = Column(Boolean, default=False)

# --- Pydantic моделі ---
class CharacterBase(BaseModel):
    name: str
    breathing_style: str
    rank: str
    is_hashira: bool

class CharacterCreate(CharacterBase):
    pass

class CharacterRead(CharacterBase):
    id: int

    class Config:
        from_attributes = True
app = FastAPI(title="Demon Slayer Characters API")
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/characters/", response_model=CharacterRead)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

@app.get("/characters/{character_id}", response_model=CharacterRead)
def get_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@app.get("/characters/", response_model=list[CharacterRead])
def get_characters(db: Session = Depends(get_db)):
    return db.query(Character).all()