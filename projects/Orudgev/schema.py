from pydantic import BaseModel, Field

class ParrotInfo(BaseModel):
    i_parrot: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    color: str = Field(..., min_length=1)
    age: int = Field(...)

class ParrotCreate(BaseModel):
    name: str = Field(..., min_length=1)
    color: str = Field(..., min_length=1)
    age: int = Field(...)
#parrot = ParrotInfo( i_parrot=1, name='Kesha', color='purple', age=5)
#print(parrot)



