import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DB_NAME = "cars.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL
            );
            """
        )
        conn.commit()


create_table()

app = FastAPI()


class CarCreate(BaseModel):
    brand: str = Field(..., min_length=2, max_length=50, description="Car brand name (min 2, max 50 characters)")
    model: str = Field(..., min_length=1, max_length=50, description="Car model name (min 1, max 50 characters)")
    year: int = Field(..., ge=1886, le=2100, description="Year of manufacture (must be between 1886 and 2100)")


class CarResponse(BaseModel):
    id: int
    brand: str
    model: str
    year: int

    class Config:
        orm_mode = True


@app.post("/cars/", response_model=CarResponse)
def create_car(car: CarCreate):
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO cars (brand, model, year) VALUES (?, ?, ?)",
            (car.brand, car.model, car.year),
        )
        conn.commit()
        car_id = cursor.lastrowid
        car_data = conn.execute(
            "SELECT id, brand, model, year FROM cars WHERE id = ?",
            (car_id,),
        ).fetchone()
    return dict(car_data)


@app.get("/cars/{car_id}", response_model=CarResponse)
def get_car(car_id: int):
    with get_connection() as conn:
        car = conn.execute(
            "SELECT id, brand, model, year FROM cars WHERE id = ?",
            (car_id,),
        ).fetchone()
        if car is None:
            raise HTTPException(status_code=404, detail="Car not found")
    return dict(car)


@app.get("/cars/", response_model=list[CarResponse])
def get_cars():
    with get_connection() as conn:
        cars = conn.execute(
            "SELECT id, brand, model, year FROM cars"
        ).fetchall()
    return [dict(car) for car in cars]
