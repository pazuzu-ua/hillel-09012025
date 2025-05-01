from fastapi import APIRouter

from models.homes import HomeAdd, HomeInfo, HomeUpdate

router = APIRouter(prefix='/homes', tags=['homes'])

# SITE/homes/
@router.post('/', response_model=HomeInfo)
def post_home(home: HomeAdd):
    ...

#отримати список домів
@router.get('/', response_model=list[HomeInfo])
def get_list_homes():
    ...

# SITE/homes/15000
@router.get('/{home_id}', response_model=HomeInfo)
def get_home(home_id: int):
    ...

@router.patch('{/home_id}', response_model=HomeInfo)
def update_home(home: HomeUpdate):
    ...

@router.delete('/{home_id}')
def delete_home(home_id: int):
    ...