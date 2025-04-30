from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    year: int

class BookCreate(BookBase):
    pass

class BookRead(BookBase):
    id: int

    model_config = {
        "from_attributes": True
    }