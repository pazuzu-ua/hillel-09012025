from datetime import date

from pydantic import BaseModel, Field


class CarsInfo(BaseModel):
    i_car: int = Field(..., gt=0)
    brand: str = Field(..., min_length=1)
    model: str = Field(..., min_length=1)
    colour: str = Field(..., min_length=1)
    production_date: date = Field(...)


class CarCreate(BaseModel):
    brand: str = Field(..., min_length=1)
    model: str = Field(..., min_length=1)
    colour: str = Field(..., min_length=1)
    production_date: date = Field(...)