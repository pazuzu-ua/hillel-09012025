from pydantic import BaseModel, Field

class AuthorBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        examples=['Stephen King'],
        description='The full name of the author',
    )
    birth_year: int = Field(
        ...,
        gt=0,
        examples=[1986],
        description='The birth year if the author'
    )

class AuthorAdd(AuthorBase):
    ...


class AuthorInfo(AuthorBase):
    i_author: int = Field(
        ...,
        gt=0,
        examples=[100],
        description='The unique ID of the author'
    )

class AuthorUpdate(AuthorBase):
    name: str | None = Field(
        None,
        min_length=1,
        max_length=100,
        examples=['Stephen King'],
        description='The full name of the author',
    )
    birth_year: int | None = Field(
        None,
        gt=0,
        examples=[1986],
        description='The birth year if the author'
    )

# example: str = Field(...)    --- параметр обов'язковий, може бути тільки стрічкою
# example: str | None = Field(...)    --- параметр обов'язковий, може бути як стрічка, так і None
# example: str | None = Field(None)    --- параметр НЕ обов'язковий, може бути як стрічка, так і None
