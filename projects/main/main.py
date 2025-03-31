from fastapi import FastAPI

from endpoints.authors import router as author_router
from endpoints.genres import router as genres_router
from endpoints.books import router as books_router
from db.common import init_db


app = FastAPI(
    title='Library API',
    description='API for the simple library.',
    version='1.5.0',
)

@app.on_event('startup')
def start_up():
    init_db()

app.include_router(author_router)
app.include_router(genres_router)
app.include_router(books_router)
