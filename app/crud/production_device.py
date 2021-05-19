from datetime import datetime
from pydantic.fields import T
from sqlalchemy.orm import Session

import pandas as pd

from app.models.production_device import Welding_equipment,Maintain_record
from app.schemas import Maintain_record as M1


class CRUDProduction_device:
    def get_list_welding_equipment(self, db: Session):
        return db.query(Welding_equipment).all()
    def get_list_maintain_record(self, db: Session):
        return db.query(Maintain_record).all()
    def add_maintain_record(self, db: Session, info:M1) ->Maintain_record:
        info.start_time=datetime.now()
        info.end_time=datetime.now()
        print(info.dict())
        db_item = Maintain_record(**info.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def update_maintain_record(self, db: Session, info:M1):
        db_item = db.query(Maintain_record).filter(Maintain_record.id == info.id).first()
        if db_item:
            update_dict = info.dict(exclude_unset=True)
            for k, v in update_dict.items():
                setattr(db_item, k, v)
            db.commit()
            db.flush()
            db.refresh(db_item)
            return db_item
    def delete_maintain_record_by_id(self, db: Session, Id:int):
        db_item = db.query(Maintain_record).filter(Maintain_record.id == Id).first()
        if db_item:
            db.delete(db_item)
            db.commit()
            db.flush()
            return db_item
        else:
            return False 
    def add_welding_equipment(self, db: Session, info:M1) ->Welding_equipment:
        info.start_time=datetime.now()
        info.end_time=datetime.now()
        print(info.dict())
        db_item = Welding_equipment(**info.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def update_welding_equipment(self, db: Session, info:M1):
        db_item = db.query(Welding_equipment).filter(Welding_equipment.id == info.id).first()
        if db_item:
            update_dict = info.dict(exclude_unset=True)
            for k, v in update_dict.items():
                setattr(db_item, k, v)
            db.commit()
            db.flush()
            db.refresh(db_item)
            return db_item
    def delete_welding_equipment_by_id(self, db: Session, Id:int):
        db_item = db.query(Welding_equipment).filter(Welding_equipment.id == Id).first()
        if db_item:
            db.delete(db_item)
            db.commit()
            db.flush()
            return db_item
        else:
            return False 
    
    def down_welding_equipment(self, db: Session):
        item_lists = self.get_list_welding_equipment(db=db)
        item_lists_dict = [i.dobule_to_dict() for i in item_lists]
        print(item_lists_dict)
        # with open('/app/file/welding_equipment.csv','wb') as f:
        #     pass
        pd.DataFrame(item_lists_dict).to_csv('welding_equipment.csv')
        return True
    def down_maintain_record(self, db: Session):
        item_lists = self.get_list_maintain_record(db=db)
        item_lists_dict = [i.dobule_to_dict() for i in item_lists]
        print(item_lists_dict)
        # with open('/app/file/welding_equipment.csv','wb') as f:
        #     pass
        pd.DataFrame(item_lists_dict).to_csv('maintain_record.csv')
        return True
        

curd_production_device = CRUDProduction_device()
