from datetime import date

from pydantic import BaseModel, Field


class CarBase(BaseModel):
    brand: str = Field(..., min_length=1, description='The brand of the car')
    model: str = Field(..., min_length=1, description='The model of the car')
    colour: str = Field(..., min_length=1, description='The colour of the car')
    production_date: date = Field(...,
                                  description='The production date of the car in the following format: "yyyy-mm-dd"')


class CarsInfo(CarBase):
    i_car: int = Field(..., gt=0, description='The unique ID of the car')


class CarCreate(CarBase):
    ...


class CarUpdate(CarBase):
    ...
