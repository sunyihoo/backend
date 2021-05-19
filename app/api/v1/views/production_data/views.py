from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm.session import Session
from starlette.responses import FileResponse

from app.core import deps
from app.utils import response_code
from app.crud import curd_production_data




router = APIRouter()

@router.get('/shift_production_data/list')
def get_list_maintain_record(db: Session = Depends(deps.get_db)):
    list = curd_production_data.get_list_shift_production_data(db=db)
    list_dict = [i.dobule_to_dict() for i in list]
    return response_code.resp_200(
        data=list_dict
    )

@router.get('/equip_production_data/list')
def get_list_maintain_record(db: Session = Depends(deps.get_db)):
    list = curd_production_data.get_list_equip_production_data(db=db)
    list_dict = [i.dobule_to_dict() for i in list]
    return response_code.resp_200(
        data=list_dict
    )

@router.get('/personnel_production_data/list')
def get_list_maintain_record(db: Session = Depends(deps.get_db)):
    list = curd_production_data.get_list_personnel_production_data(db=db)
    list_dict = [i.dobule_to_dict() for i in list]
    return response_code.resp_200(
        data=list_dict
    )

@router.get('/down_shift_production_data')
def down_shift_production_data(db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_production_data.down_shift_production_data(db=db)
    return FileResponse(
        'shift_production_data.csv',
        filename='班组生产数据.csv'
    )
@router.get('/down_equip_production_data')
def down_equip_production_data(db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_production_data.down_equip_production_data(db=db)
    return FileResponse(
        'equip_production_data.csv',
        filename='设备生产数据.csv'
    )
@router.get('/down_personnel_production_data')
def down_personnel_production_data(db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_production_data.down_personnel_production_data(db=db)
    return FileResponse(
        'personnel_production_data.csv',
        filename='人员生产数据.csv'
    )

@router.get('/welding_workers/list')
def get_list_maintain_record(db: Session = Depends(deps.get_db)):
    list = curd_production_data.get_list_welding_workers(db=db)
    list_dict = [i.dobule_to_dict() for i in list]
    return response_code.resp_200(
        data=list_dict
    )
@router.get('/down_welding_workers')
def down_welding_workers(db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_production_data.down_welding_workers(db=db)
    return FileResponse(
        'welding_workers.csv',
        filename='焊接工人管理表.csv'
    )