from pydantic import BaseModel, Field

class ParrotMain(BaseModel):
    name: str = Field(..., min_length=1)
    color: str = Field(..., min_length=1)
    age: int = Field(...)

class ParrotInfo(ParrotMain):
    i_parrot: int = Field(..., gt=0)

class ParrotCreate(ParrotMain):
    ...

class ParrotUpdate(ParrotMain):
    ...

#parrot = ParrotInfo( i_parrot=1, name='Kesha', color='purple', age=5)
#print(parrot)