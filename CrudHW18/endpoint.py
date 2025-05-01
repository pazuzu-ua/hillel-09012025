from fastapi import APIRouter, HTTPException, Response
from schema import BooksInfo, BooksCreate, BookUpdate
from db import create_book, get_list_of_books, get_book_info, remove_book, update_book_info

#method GET
#method POST

router = APIRouter(prefix='/Books', tags=['books'])


@router.post('/', response_model=BooksInfo)
def create_book_api(book: BooksCreate):
    id = create_book(book.title, book.author, book.isbn, book.year,)
    if not id:
        raise HTTPException(status_code=503, detail='book not create')
    book_info = BooksInfo(
        id=id,
        title=book.title,
        author=book.author,
        isbn=book.isbn,
        year=book.year,
    )
    return book_info


@router.get('/', response_model=list[BooksInfo])
def get_books_list():
    books_list = get_list_of_books()
    books_list = [BooksInfo(id=book[0], title=book[1], author=book[2], isbn=book[3], year=book[4]) for book in books_list]
    return books_list


router1 = APIRouter(prefix='/Books', tags=['Books funktion'])


@router1.get('/{book_id}', response_model=BooksInfo)
def get_books_info(book_id: int):

    book_data = get_book_info(book_id)
    if not book_data:
        raise HTTPException(status_code=404, detail='Book not found')
    book = BooksInfo(
        id=book_data[0],
        title=book_data[1],
        author=book_data[2],
        isbn=book_data[3],
        year=book_data[4]
    )
    return book


@router1.delete('/{book_id}', status_code=204)
def delete_book(book_id: int):
    book_data = get_book_info(book_id)
    if not book_data:
        raise HTTPException(status_code=404, detail='Book not found')
    remove_book(book_id)
    return Response(status_code=204)


@router1.put('/{book_id}', response_model=BooksInfo)
def update_book(book: BookUpdate, book_id: int):
    book_data = get_book_info(book_id)
    if not book_data:
        raise HTTPException(status_code=404, detail='Book not found')

    update_book_info(book_id, book)

    updated_data = get_book_info(book_id)
    book_info = BooksInfo(
        id=updated_data[0],
        title=updated_data[1],
        author=updated_data[2],
        isbn=updated_data[3],
        year=updated_data[4],
    )
    return book_info
