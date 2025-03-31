from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=250,
        examples=['Harry Potter and the Philosopers Stone'],
        description='The title of the book',
    )
    publication_year: int = Field(
        ...,
        gt=1500,
        examples=[1986],
        description='The publication year of the book'
    )
    pages: int = Field(
        ...,
        gt=0,
        examples=[700],
        description='The number of pages of the book'
    )
    i_author: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the author'
    )
    i_genre: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the genre'
    )

class BookAdd(BookBase):
    ...


class BookInfo(BookBase):
    i_book: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the book'
    )

class BookUpdate(BookBase):
    title: str | None = Field(
        None,
        min_length=1,
        max_length=250,
        examples=['Harry Potter and the Philosopers Stone'],
        description='The title of the book',
    )
    publication_year: int = Field(
        1550,                   # тепер цей параметр теж не обов'язковий
        gt=1500,
        examples=[1986],
        description='The publication year of the book'
    )
    pages: int | None = Field(
        None,
        gt=0,
        examples=[700],
        description='The number of pages of the book'
    )
    i_author: int | None = Field(
        None,
        gt=0,
        examples=[100],
        description='The unique ID of the author'
    )
    i_genre: int | None = Field(
        None,
        gt=0,
        examples=[100],
        description='The unique ID of the genre'
    )
