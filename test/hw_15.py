from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI(
    debug=True,
    title='Car API',
    description='A simple car API',
    version='0.0.1'
)


class CarInfo(BaseModel):
    id: int = Field(
        ...,
        description='The unique ID of the car',
        gt=0
    )
    name: str = Field(
        ...,
        description='The name of the car',
        min_length=1,
        max_length=25,

    )


@app.get('/cars',
         summary='Get a list of cars',
         description='Retrieve a list of all the cars',
         response_model=list[dict])
async def get_cars():
    return [
        {'id': 1, 'brand': 'Tesla', 'colour': 'white'},
        {'id': 2, 'brand': 'BMW', 'colour': 'black'},
        {'id': 3, 'brand': 'Lamborghini', 'colour': 'yellow'},
    ]


@app.get('/car/{car_id}',
         summary='Get car info',
         description='Get info on a single car')
async def get_car(car_id: int):
    return CarInfo(
        id=car_id,
        name='Name of the car'
    )
