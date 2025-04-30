from fastapi import APIRouter, HTTPException, Response

from schema import ParrotInfo, ParrotCreate, ParrotUpdate

from db import create_parrot, get_list_of_parrots, get_parrot_info, delete_parrot, update_parrot_info

router = APIRouter(prefix='/parrots', tags=['parrots'])

@router.get('/', response_model=list[ParrotInfo])
def get_parrots_list():
    parrots_list = get_list_of_parrots()
    parrots_list = [ParrotInfo(i_parrot=parrot[0], name=parrot[1], color=parrot[2], age=parrot[3]) for parrot in parrots_list]
    return parrots_list

@router.post('/', response_model=ParrotInfo)
def create_parrot_endpoint(parrot: ParrotCreate):
    parrot_id = create_parrot(parrot.name, parrot.color, parrot.age)
    if not parrot_id:
        raise HTTPException(status_code=404, detail='Parrot not created')

    return ParrotInfo(
        i_parrot=parrot_id,
        name=parrot.name,
        color=parrot.color,
        age=parrot.age
    )

@router.get('/{parrot_id}', response_model=ParrotInfo)
def get_parrots_info(parrot_id: int):
    parrot_info = get_parrot_info(parrot_id)
    if not parrot_info:
        raise HTTPException(status_code=404, detail='Parrot not found')
    parrot_info = ParrotInfo(i_parrot=parrot_info[0], name=parrot_info[1], color=parrot_info[2], age=parrot_info[3])
    return parrot_info

@router.delete('/{parrot_id}', status_code=204)
def delete_parrot_endpoint(parrot_id: int):
    parrot_info = get_parrot_info(parrot_id)
    if not parrot_info:
        raise HTTPException(status_code=404, detail='Parrot not found')
    delete_parrot(parrot_id)
    return Response(status_code=204)

@router.put('/{parrot_id}', response_model=ParrotInfo)
def update_parrot(parrot: ParrotUpdate, parrot_id: int):
    parrot_info = get_parrot_info(parrot_id)
    if not parrot_info:
        raise HTTPException(status_code=404, detail='Parrot not found')
    update_parrot_info(parrot_id, parrot)

    parrot_info = get_parrot_info(parrot_id)

    return ParrotInfo(
        i_parrot=parrot_id,
        name=parrot.name,
        color=parrot.color,
        age=parrot.age
    )