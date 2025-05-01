from pydantic import BaseModel, Field


class HomeBase(BaseModel):
    street_name: str = Field(
        ...,
        min_length=1,
        max_length=250,
        examples=['Harry Potter'],
        description='The street_name of the home'
    )
    apartment_number: int = Field(
        ...,
        gt=1500,
        examples=[1501],
        description='The apartment_number of the home'
    )
    floor: int = Field(
        ...,
        gt=0,
        examples=[10],
        description='The number of floor of the home'
    )
    i_cat: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the cat'
    )
    i_toy: int = Field(
        ...,
        gt=0,
        examples=[1985],
        description='first appearance of the toy(year)'
    )

class HomeAdd(HomeBase):
    street_name: str = Field(
        ...,
        min_length=1,
        max_length=250,
        examples=['Harry Potter'],
        description='The street_name of the home'
    )
    apartment_number: int = Field(
        ...,
        gt=1500,
        examples=[1501],
        description='The apartment_number of the home'
    )
    floor: int = Field(
        ...,
        gt=0,
        examples=[10],
        description='The number of floor of the home'
    )
    i_cat: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the cat'
    )
    i_toy: int = Field(
        ...,
        gt=0,
        examples=[1985],
        description='first appearance of the toy(year)'
    )

class HomeInfo(HomeBase):
    i_home: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the home'
    )

class HomeUpdate(HomeBase):
    street_name: str | None = Field(
        None,
        min_length=1,
        max_length=250,
        examples=['Harry Potter'],
        description='The street_name of the home'
    )
    apartment_number: int | None = Field(
        None,
        gt=0,
        examples=[111],
        description='The apartment_number at the home'
    )
    floor: int | None = Field(
        None,
        gt=0,
        examples=[10],
        description='The number of floor at the home'
    )
    i_cat: int | None = Field(
        None,
        gt=0,
        examples=[100],
        description='The unique ID of the cat'
    )
    i_toy: int | None = Field(
        None,
        gt=0,
        examples=[100],
        description='The unique ID of the toy'
    )