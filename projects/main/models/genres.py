from pydantic import BaseModel, Field


class GenreBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=25,
        examples=['horror'],
        description='The name of the genre',
    )

class GenreAdd(GenreBase):
    ...

class GenreInfo(GenreBase):
    i_genre: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the genre'
    )

class GenreUpdate(GenreBase):
    name: str | None = Field(
        None,
        min_length=1,
        max_length=25,
        examples=['horror'],
        description='The name of the genre',
    )
