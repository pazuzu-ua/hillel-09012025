from pydantic import BaseModel, Field, conint, constr
from typing import List

class Book(BaseModel):
    title: constr(min_length=1, max_length=100)
    pages: conint(gt=0, lt=10000)

class Library(BaseModel):
    name: constr(min_length=3, max_length=50)
    books: List[Book]
