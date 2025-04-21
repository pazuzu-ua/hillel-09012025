# Authors
# i_author, name, surname, birth_date
#
# main.py   ------ ( db.py, schema.py, endpoints.py )
from fastapi import FastAPI

from db import init_db
from endpoint import router


app = FastAPI(
    title='Cats Catologue',
    description='The catologue of faworite cats toys.',
    on_startup=[init_db] # усі ці функції будуть запущені ПЕРЕД стартом програми
)

app.include_router(router)