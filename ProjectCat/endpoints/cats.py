from fastapi import APIRouter

from models.cats import CatAdd, CatInfo, CatUpdate
from db.cats import add_cat


router = APIRouter(prefix='/cats', tags=['cats'])

# SITE/cats/
@router.post('/', response_model=CatInfo)
def post_cat(cat: CatAdd):
    ...
#add_cat(cat.name, cat.birth_year, cat.years, cat.owner)

#отримати список авторів
@router.get('/', response_model=list[CatInfo])
def get_list_cats():
    ...

# SITE/cats/15000
@router.get('/{cats_id}', response_model=CatInfo)
def get_cat(cat_id: int):
    ...

@router.patch('{/cat_id}', response_model=CatInfo)
def update_cat(cat: CatUpdate):
    ...

@router.delete('/cats_id}')
def delete_cat(cat_id: int):
    ...
