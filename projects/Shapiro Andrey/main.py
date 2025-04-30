from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int

cars_db = []
current_id = 1

@app.post("/cars/", response_model=Car)
def create_car(car: Car):
    global current_id
    car.id = current_id
    cars_db.append(car)
    current_id += 1
    return car

@app.get("/cars/{car_id}", response_model=Car)
def get_car(car_id: int):
    for car in cars_db:
        if car.id == car_id:
            return car
    raise HTTPException(status_code=404, detail="Машина с таким ID не найдена")

@app.get("/cars/", response_model=list[Car])
def get_cars():
    return cars_db



