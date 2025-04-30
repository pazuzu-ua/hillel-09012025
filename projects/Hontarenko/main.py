from fastapi import FastAPI

from db.cars import init_db

from endpoints.cars import router




app = FastAPI(
    title='Cars Catalogue',
    description='The catalogue of cars',
    on_startup=[init_db]
)

app.include_router(router)