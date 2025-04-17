from fastapi import FastAPI
from pydantic import BaseModel

# Створюємо FastAPI-додаток з метаданими
app = FastAPI(
    title="Мій перший FastAPI-проєкт",
    description="Це приклад API, який демонструє основи FastAPI",
    version="1.0.0"
)

@app.get("/books")
def get_books():
    return {
        "books": [
            {"title": "Harry Potter", "author": "J.K. Rowling"},
            {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
        ]
    }

class Author(BaseModel):
    name: str
    age: int
    books_written: list[str]

@app.get("/author", response_model=Author)
def get_author():
    return Author(
        name="George Orwell",
        age=46,
        books_written=["1984", "Animal Farm"]
    )