from fastapi import APIRouter

from models.toys import ToyAdd, ToyInfo, ToyUpdate

router = APIRouter(prefix='/toys', tags=['toys'])

# SITE/toys/
@router.post('/', response_model=ToyInfo)
def post_toy(toy: ToyAdd):
    ...

#отримати список іграшок
@router.get('/', response_model=list[ToyInfo])
def get_list_toys():
    ...

# SITE/toys/15000
@router.get('/{toy_id}', response_model=ToyInfo)
def get_toy(toy_id: int):
    ...

@router.patch('{/toy_id}', response_model=ToyInfo)
def update_toy(toy: ToyUpdate):
    ...

@router.delete('/{toy_id}')
def delete_toy(toy_id: int):
    ...
