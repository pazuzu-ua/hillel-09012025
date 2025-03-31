from fastapi import APIRouter

from models.authors import AuthorAdd, AuthorInfo, AuthorUpdate
from db.authors import add_author


router = APIRouter(prefix='/authors', tags=['authors'])

# 127.0.0.1:5000/authors/
@router.post('/', response_model=AuthorInfo)
def post_author( author: AuthorAdd ):
    ...

@router.get('/', response_model=list[AuthorInfo])
def get_list_author():
    ...

# 127.0.0.1:5000/authors/15500
@router.get( '/{author_id}', response_model=AuthorInfo )
def get_author( author_id: int ):
    ...

@router.patch('/{author_id}', response_model=AuthorInfo )
def update_author( author_id: int, author: AuthorUpdate ):
    ...

@router.delete('/{author_id}')
def delete_author( author_id: int ):
    ...
