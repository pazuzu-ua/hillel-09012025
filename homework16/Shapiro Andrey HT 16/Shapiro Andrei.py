from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    pages: int = Field(..., gt=0, lt=10000)

class Library(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    books_list: list[Book]
