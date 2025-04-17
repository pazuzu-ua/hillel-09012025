from pydantic import BaseModel, Field


class Book(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    pages: int = Field(..., gt=1, le=10000)


class Library(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    books: list[Book] = Field(default_factory=list)

