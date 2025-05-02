from fastapi import FastAPI

from db import init_db
from endpoint import router

app = FastAPI(
    title='Anime Catalogue',
    description='A catalogue of anime series.',
    on_startup=[init_db]
)

app.include_router(router)
