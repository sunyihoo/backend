import pandas as pd
from sqlalchemy.orm import Session

from app.models.welding_equipment import Shift_welding,Equip_welding,Personnel_welding

class CRUDWelding_equipment:
    def get_list_shift_welding(self, db: Session):
        return db.query(Shift_welding).all()
    def get_list_equip_welding(self, db: Session):
        return db.query(Equip_welding).all()
    def get_list_personnel_welding(self, db: Session):
        return db.query(Personnel_welding).all()
    def down_shift_welding(self, db: Session):
        item_lists = self.get_list_shift_welding(db=db)
        item_lists_dict = [i.dobule_to_dict() for i in item_lists]
        print(item_lists_dict)
        pd.DataFrame(item_lists_dict).to_csv('shift_welding.csv')
        return True
    def down_equip_welding(self, db: Session):
        item_lists = self.get_list_equip_welding(db=db)
        item_lists_dict = [i.dobule_to_dict() for i in item_lists]
        print(item_lists_dict)
        pd.DataFrame(item_lists_dict).to_csv('equip_welding.csv')
        return True
    def down_personnel_welding(self, db: Session):
        item_lists = self.get_list_personnel_welding(db=db)
        item_lists_dict = [i.dobule_to_dict() for i in item_lists]
        print(item_lists_dict)
        pd.DataFrame(item_lists_dict).to_csv('personnel_welding.csv')
        return True
             

curd_welding_equipment = CRUDWelding_equipment()
