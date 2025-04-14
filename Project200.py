from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Книжковий API",
    description="Цей API дозволяє отримати інформацію про книги та авторів.",
    version="1.0.0"
)


class Author(BaseModel):
    id: int
    name: str
    nationality: str


@app.get("/books")
def get_books():
    return {
        "books": [
            {"id": 1, "title": "Майстер і Маргарита", "author": "Михайло Булгаков"},
            {"id": 2, "title": "Злочин і кара", "author": "Федір Достоєвський"},
        ]
    }


@app.get("/author", response_model=Author)
def get_author():
    return Author(id=1, name="Лев Толстой", nationality="Україна")
