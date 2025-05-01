#uvicorn main:app --reload
from fastapi import FastAPI

from endpoints.cats import router as cat_router
from endpoints.toys import router as toy_router
from endpoints.homes import router as home_router

from db.common import init_db

app = FastAPI(
    title='Library API',
    description='API for the simple library',
    version='1.0.0',
)

@app.on_event('startup')
def start_up():
    init_db()

app.include_router(cat_router)
app.include_router(toy_router)
app.include_router(home_router)
