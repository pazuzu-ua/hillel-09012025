from fastapi import FastAPI
from db import init_db
from endpoints import router

app = FastAPI(
    title="The World of Parrots",
    description="World about parrots",
    on_startup=[init_db]
)

app.include_router(router)