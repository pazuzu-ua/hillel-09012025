from fastapi import APIRouter

from models.genres import GenreAdd, GenreInfo, GenreUpdate


router = APIRouter(prefix='/genres', tags=['genres'])

# 127.0.0.1:5000/genres/
@router.post('/', response_model=GenreInfo)
def post_genre( author: GenreAdd ):
    ...

@router.get('/', response_model=list[GenreInfo])
def get_list_genre():
    ...

# 127.0.0.1:5000/genres/15500
@router.get( '/{genre_id}', response_model=GenreInfo )
def get_genre( genre_id: int ):
    ...

@router.patch('/{genre_id}', response_model=GenreInfo )
def update_genre( genre_id: int, genre: GenreUpdate ):
    ...

@router.delete('/{genre_id}')
def delete_genre( genre_id: int ):
    ...
