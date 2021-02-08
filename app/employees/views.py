from fastapi import APIRouter
from app.employees.models import Employee

router = APIRouter(
    prefix='/employees',
    tags=['employees'],
    responses={
        404: {'description': 'Not found'}
    },
)


@router.post('/create')
async def create_employees(employee: Employee):
    return employee


@router.get('/')
async def get_all_employees():
    return [
        {
            'Testing': 'KAKAK'
        }
    ]


@router.get('/{employee_id}')
async def read_item(employee_id: int):
    return {'employee_id': employee_id}
