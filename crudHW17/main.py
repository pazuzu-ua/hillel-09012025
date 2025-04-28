from fastapi import FastAPI
from db import init_db
from endpoint import router

app = FastAPI(
    title='books Archive',
    description='Here is located many books',
    on_startup=[init_db],
    debug=True
)
app.include_router(router)




