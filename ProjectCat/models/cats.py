from pydantic import BaseModel, Field

class CatBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        examples=['Luna'],
        description='The full name of the cats'
    )
    birth_year: int = Field(
        ...,
        gt=0,
        examples=[2022],
        description='The birth year of the cat'
    )
    years: int = Field(
        gt=0,
        examples=[3],
        description='The years of the cat'
    )
    owner: str | None = Field(
        None,
        min_length=1,
        max_length=100,
        examples=['Egor'],
        description='The full name of the owners'
    )

class CatAdd(CatBase):
    name: str = Field(
        min_length=1,
        max_length=100,
        examples=['Luna'],
        description='The full name of the cats'
    )
    birth_year: int = Field(
        gt=0,
        examples=[2022],
        description='The birth year of the cat'
    )
    years: int = Field(
        gt=0,
        examples=[3],
        description='The years of the cat'
    )
    owner: str | None = Field(
        None,
        min_length=1,
        max_length=100,
        examples=['Egor'],
        description='The full name of the owners'
    )

class CatInfo(CatBase):
    i_cat: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the cat'
    )

class CatUpdate(CatBase):
    name: str | None = Field(
        None,
        min_length=1,
        max_length=100,
        examples=['Luna'],
        description='The full name of the cats'
    )
    birth_year: int | None = Field(
        None,
        gt=0,
        examples=[2022],
        description='The birth year of the cat'
    )
    years: int | None = Field(
        None,
        gt=0,
        examples=[3],
        description='The years of the cat'
    )
    owner: str | None = Field(
        None,
        min_length=1,
        max_length=100,
        examples=['Egor'],
        description='The full name of the owners'
    )

#example: str = Field(...)     ---     параметр обов'язковий, може бути тільки стрічка
#example: str | None = Field(...)     ---     параметр обов'язковий, може бути як стрічка, так і нічого
#example: str | None = Field(None)     ---     параметр  НЕ обов'язковий, може бути як стрічка, так і нічого