from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm.session import Session

from app.core import deps
from app.utils import response_code
from app.crud import curd_production_device


router = APIRouter()

@router.post('/production_data')
def recv_production_data(data,recv):
    # {"wd":recv}:
    print(data)
    return {"data":data}
