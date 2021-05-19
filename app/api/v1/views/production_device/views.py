from logging import info
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm.session import Session
from fastapi.responses import FileResponse

from app.core import deps
from app.utils import response_code
from app.crud import curd_production_device

from app.schemas import Maintain_record,Welding_equipment


router = APIRouter()

@router.get('/maintain_record/list')
def get_list_maintain_record(db: Session = Depends(deps.get_db)):
    list = curd_production_device.get_list_maintain_record(db=db)
    list_dict = [i.dobule_to_dict() for i in list]
    return response_code.resp_200(
        data=list_dict
    )

@router.get('/welding_equipment/list')
def get_list_maintain_record(db: Session = Depends(deps.get_db)):
    list = curd_production_device.get_list_welding_equipment(db=db)
    list_dict = [i.dobule_to_dict() for i in list]
    return response_code.resp_200(
        data=list_dict
    )
@router.post('/add_maintain_record')
def add_maintain_record(info:Maintain_record, db: Session = Depends(deps.get_db)):
    db_item = curd_production_device.add_maintain_record(db=db,info=info)
    if db_item:
        return response_code.resp_200(data=db_item.dobule_to_dict())

@router.post('/update_maintain_record')
def update_maintain_record(info:Maintain_record, db: Session = Depends(deps.get_db)):
    db_item = curd_production_device.update_maintain_record(db=db,info=info)
    if db_item:
        return response_code.resp_200(data=db_item.dobule_to_dict())
    else:
        return response_code.resp_400(data='info is false')

@router.post('/delete_maintain_record')
def delete_maintain_record(info:Maintain_record, db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_production_device.delete_maintain_record_by_id(Id=info.id,db=db)
    if result:
        return response_code.resp_200(data=result.dobule_to_dict())
    else:
        return response_code.resp_400(data='NOt this info')

@router.post('/add_welding_equipment')
def add_welding_equipment(info:Welding_equipment, db: Session = Depends(deps.get_db)):
    db_item = curd_production_device.add_welding_equipment(db=db,info=info)
    if db_item:
        return response_code.resp_200(data=db_item.dobule_to_dict())

@router.post('/update_welding_equipment')
def update_welding_equipment(info:Welding_equipment, db: Session = Depends(deps.get_db)):
    db_item = curd_production_device.update_welding_equipment(db=db,info=info)
    if db_item:
        return response_code.resp_200(data=db_item.dobule_to_dict())
    else:
        return response_code.resp_400(data='info is false')

@router.post('/delete_welding_equipment')
def delete_welding_equipment(info:Welding_equipment, db: Session = Depends(deps.get_db)):
    print(info.dict())
    result=curd_production_device.delete_welding_equipment_by_id(Id=info.id,db=db)
    if result:
        return response_code.resp_200(data=result.dobule_to_dict())
    else:
        return response_code.resp_400(data='NOt this info')
@router.get('/down_welding_equipment')
def down_welding_equipment(db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_production_device.down_welding_equipment(db=db)
    return FileResponse(
        'welding_equipment.csv',
        filename='焊机设备管理表.csv'
    )

@router.get('/down_maintain_record')
def down_welding_equipment(db: Session = Depends(deps.get_db)):
    # print(info.dict())
    result=curd_production_device.down_maintain_record(db=db)
    return FileResponse(
        'maintain_record.csv',
        filename='维修记录管理表.csv'
    )