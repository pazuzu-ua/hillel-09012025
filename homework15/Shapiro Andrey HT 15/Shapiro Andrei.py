from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
title = "Books Storage"
description = "A storage which contains many types of books"
version = "2.0.0"

class Book(BaseModel):
    title: str
    author: str
    year: int

@app.get("/books")
def get_books():
    return {"books": [
        {"title": "Book 1", "author": "Author 1", "year": 2001},
        {"title": "Book 2", "author": "Author 2", "year": 2005},
    ]}

@app.get("/books/{book_id}",
response_model=Book)
def get_book(book_id: int):
    return {"title": f"Book {book_id}", "author": f"Author {book_id}", "year": 2000 + book_id}