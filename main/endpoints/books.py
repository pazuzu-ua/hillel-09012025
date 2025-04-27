from fastapi import APIRouter

from models.books import BookAdd, BookInfo, BookUpdate


router = APIRouter(prefix='/books', tags=['books'])

# 127.0.0.1:5000/genres/
@router.post('/', response_model=BookInfo)
def post_book( author: BookAdd ):
    ...

@router.get('/', response_model=list[BookInfo])
def get_list_book():
    ...

# 127.0.0.1:5000/genres/15500
@router.get( '/{book_id}', response_model=BookInfo )
def get_book( book_id: int ):
    ...

@router.patch('/{book_id}', response_model=BookInfo )
def update_book( book_id: int, genre: BookUpdate ):
    ...

@router.delete('/{book_id}')
def delete_book( book_id: int ):
    ...
