from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm.session import Session
from starlette.responses import FileResponse

from app.core import deps
from app.utils import response_code
from app.crud import curd_welding_equipment




router = APIRouter()

@router.get('/shift_welding/list')
def get_list_maintain_record(db: Session = Depends(deps.get_db)):
    list = curd_welding_equipment.get_list_shift_welding(db=db)
    list_dict = [i.dobule_to_dict() for i in list]
    return response_code.resp_200(
        data=list_dict
    )

@router.get('/equip_welding/list')
def get_list_maintain_record(db: Session = Depends(deps.get_db)):
    list = curd_welding_equipment.get_list_equip_welding(db=db)
    list_dict = [i.dobule_to_dict() for i in list]
    return response_code.resp_200(
        data=list_dict
    )

@router.get('/personnel_welding/list')
def get_list_maintain_record(db: Session = Depends(deps.get_db)):
    list = curd_welding_equipment.get_list_personnel_welding(db=db)
    list_dict = [i.dobule_to_dict() for i in list]
    return response_code.resp_200(
        data=list_dict
    )
@router.get('/down_shift_welding')
def down_shift_welding(db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_welding_equipment.down_shift_welding(db=db)
    return FileResponse(
        'shift_welding.csv',
        filename='shift_welding.csv'
    )
@router.get('/down_personnel_welding')
def down_personnel_welding(db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_welding_equipment.down_personnel_welding(db=db)
    return FileResponse(
        'personnel_welding.csv',
        filename='personnel_welding.csv'
    )
@router.get('/down_equip_welding')
def down_equip_welding(db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_welding_equipment.down_equip_welding(db=db)
    return FileResponse(
        'equip_welding.csv',
        filename='equip_welding.csv'
    )