from fastapi import FastAPI
from pydantic import BaseModel, Field

# pip install fastapi
# pip install uvicorn
# uvicorn main:app --reload
app = FastAPI(
    debug=True,         # помилки стануть більш детальними
    title='Book API',
    description='A simple book API',
    version='0.0.3',
)

# обробник шляху
# BOOK - entity - сутність
# /books      - GET - отримати УСЮ колекцію
# /books      - POST - створити 1 елемент
# параметри шляху: {name}
# /books/{id}  - GET  - отримати інфу по 1 книжці
# /books/{id}  - PATCH - оновити інфу по 1 книжці
# /books/{id}  - DELETE - видалити 1 з книжок

# @app.get('/')                       # root = корінь сайту
# async def index():                  # ключове слово async робить ф-ію асинхронною
#     return "Hello"
#
# @app.get('/book')                       # root = корінь сайту
# async def get_book():                  # ключове слово async робить ф-ію асинхронною
#     return "Hello"

class BookInfo(BaseModel):      # базова модель книги
    # id: int                     # поле id, типу int
    # перший параметр - це значення за замовчуванням
    # ... - це без значення за замовчуванням - параметр є обов'язковим
    id: int = Field(..., description='The unique ID of the book', gt=0)
    name: str = Field(..., description='The name of the book', min_length=1, max_length=50)

@app.get(
    '/books',
    summary='Get a list of books',
    description='Retrieve a list of all the books',
    response_model=list[dict],
)
async def get_books():
    return [
        { "id": 1, "name": "HarryPotter" },
        { "id": 2, "name": "IT" },
        { "id": 3, "name": "HarryPotter2" },
    ]

#  /customers/{customer_id}/products/{product_id}
# /customers/104/products/56
@app.get(
    '/books/{book_id}',
    summary='Get book info',
    description='Get info on a single book.',
    response_model=BookInfo
)
async def get_book(book_id: int):
    return BookInfo(
        id=book_id,
        name="*" * 51
    )
