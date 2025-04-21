# Cats
# i_cat, name, breed, birth_date
from datetime import date

from pydantic import BaseModel, Field


class CatInfo(BaseModel):
    i_author: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    breed: str = Field(..., min_length=1)
    birth_date: date = Field(...)


class CatCreate(BaseModel):
    name: str = Field(..., min_length=1)
    breed: str = Field(..., min_length=1)
    birth_date: date = Field(...)



