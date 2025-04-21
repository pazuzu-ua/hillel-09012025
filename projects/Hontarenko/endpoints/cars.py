from schemas.cars import CarsInfo, CarCreate
from fastapi import APIRouter, HTTPException
from db.cars import create_car, get_list_of_cars,get_car_info

router = APIRouter(prefix='/cars', tags=['cars'])


@router.get('/', response_model=list[CarsInfo])
def get_car_list():
    cars_list = get_list_of_cars()
    cars_list=[CarsInfo(i_car=car[0], brand=car[1], model=car[2], colour=car[3], production_date=car[4]) for car in cars_list]

    return cars_list


@router.get('/{car_id}', response_model=CarsInfo)
def get_car_info(car_id: int):
    car_info=get_car_info(car_id)
    if not car_info:
        raise HTTPException(status_code=404, detail=' Car not found ')
    car_info=CarsInfo(i_car=car_info[0], brand=car_info[1], model=car_info[2], colour=car_info[3], production_date=car_info[4])
    return car_info


@router.post('/', response_model=CarsInfo)
def create_car(car: CarCreate):
    car_id = create_car(car.brand, car.model, car.colour, car.production_date)
    if not car_id:
        raise HTTPException(status_code=503, detail='car not created')
    car_info = CarsInfo(
        i_car=car_id,
        brand=car.brand,
        model=car.model,
        production_date=car.production_date
    )
    return car_info