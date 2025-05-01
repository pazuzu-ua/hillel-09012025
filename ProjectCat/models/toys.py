from pydantic import BaseModel, Field


class ToyBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=25,
        examples=['Mouse'],
        description='The name of the Toy'
    )

class ToyAdd(ToyBase):
    name: str | None = Field(
        ...,
        min_length=1,
        max_length=25,
        examples=['Mouse'],
        description='The name of the Toy'
    )

class ToyInfo(ToyBase):
    i_Toy: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the toy'
    )

class ToyUpdate(ToyBase):
    name: str | None = Field(
        ...,
        min_length=1,
        max_length=25,
        examples=['Mouse'],
        description='The name of the Toy'
    )
