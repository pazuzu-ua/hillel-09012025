#Books
# id, title, author, isbn, year
from datetime import date
from pydantic import BaseModel, Field


class BooksInfo(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=50)
    isbn: int = Field(..., gt=7, ge=14)
    year: date = Field(...)


class BooksCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=50)
    isbn: int = Field(..., gt=8, ge=14)
    year: date = Field(...)


