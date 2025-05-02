from fastapi import APIRouter, HTTPException

from schema import AnimeInfo, AnimeCreate
from db import create_anime, get_list_of_anime, get_anime_info

router = APIRouter(prefix='/anime', tags=['anime'])

@router.post('/', response_model=AnimeInfo)
def create_anime_item(anime: AnimeCreate):
    anime_id = create_anime(anime.title, anime.author, anime.description)
    if not anime_id:
        raise HTTPException(status_code=503, detail='Anime not created')
    return AnimeInfo(i_anime=anime_id, **anime.dict())

@router.get('/', response_model=list[AnimeInfo])
def get_anime_list():
    anime_list = get_list_of_anime()
    return [AnimeInfo(i_anime=a[0], title=a[1], author=a[2], description=a[3]) for a in anime_list]

@router.get('/{anime_id}', response_model=AnimeInfo)
def get_anime_by_id(anime_id: int):
    anime = get_anime_info(anime_id)
    if not anime:
        raise HTTPException(status_code=404, detail='Anime not found')
    return AnimeInfo(i_anime=anime[0], title=anime[1], author=anime[2], description=anime[3])
