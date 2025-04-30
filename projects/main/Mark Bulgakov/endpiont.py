# CRUD
from fastapi import APIRouter, HTTPException

from schema import CatInfo, CatCreate
from db import create_cat, get_list_of_cats, get_cat_info

# our router:
router = APIRouter(prefix='/cats', tags=['cats'])


# ------------------ C - CREATE
# method POST:
# 127.0.0.1:5000/cats/
@router.post('/', response_model=CatInfo)
#                   змінна: МОДЕЛЬ
# КОРИСТУВАЧ МУСИТИМЕ ВВЕСТИ ЦІ ДАНІ
def create_cats(cat: CatCreate):
    cat_id = create_cat(cat.name, cat.breed, cat.birth_date)
    if not cat_id:
        raise HTTPException(status_code=503, detail='Cat not created')
    cat_info = CatInfo(
        i_cat=cat_id,
        name=cat.name,
        breed=cat.surname,
        birth_date=cat.birth_date,
    )
    return cat_info


# ------------------ R - READ
# get_info / get_list
# method GET:
# @router.метод ( шлях, моделька_для_відповіді )
# шлях: 127.0.0.1:5000    + router_prefix (/authors) + get('/')
# 127.0.0.1:5000/authors/
@router.get('/', response_model=list[CatInfo])
def get_cats_list():
    cats_list = get_list_of_cats()
    authors_list = [CatInfo(i_cat=cat[0], name=cat[1], breed=cat[2], birth_date=cat[3]) for cat
                    in cats_list]

    return cats_list


# method GET:
# 127.0.0.1:5000/authors/{author_id}
# 127.0.0.1:5000/authors/1
# 127.0.0.1:5000/authors/25
@router.get('/{cat_id}', response_model=CatInfo)
def get_cat_info(cat_id: int):
    cat_info = get_cat_info(cat_id)
    if not cat_info:
        raise HTTPException(status_code=404, detail='Author not found')
    cat_info = CatInfo(i_cat=cat_info[0], name=cat_info[1], breed=cat_info[2],
                             birth_date=cat_info[3])

    return cat_info

