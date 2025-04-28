from fastapi import APIRouter, HTTPException
from schema import BooksInfo, BooksCreate
from db import create_book, get_list_of_books, get_book_info

#method GET
#method POST

router = APIRouter(prefix='/books', tags=['books'])

@router.post('/', response_model=BooksInfo)
def create_book_api(book: BooksCreate):
    id = create_book(book.title, book.author, book.isbn, book.year,)
    if not id:
        raise HTTPException(status_code=503, detail='book not create')
    book_info = BooksInfo(
        book_id=id,
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

@router.get('/{book_id}', response_model=BooksInfo)
def get_books_info(book_id: int):

    book_data = get_book_info(book_id)
    if not book_data:
        raise HTTPException(status_code=404, detail='Book not found')



    book = BooksInfo(id=1,
                     title='Hary Potter',
                     author='J.K. Rowling',
                     isbn=123456789,
                     year='2025-04-05'
                     )
    return book


