from pydantic import BaseModel, Field

class AnimeInfo(BaseModel):
    i_anime: int = Field(..., gt=0)
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

class AnimeCreate(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
