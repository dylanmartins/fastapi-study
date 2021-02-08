from fastapi import APIRouter

router = APIRouter(tags=['healthcheck'])

@router.get('/healthcheck/')
async def get_healthcheck():
    return {'healthcheck': 'OK'}
