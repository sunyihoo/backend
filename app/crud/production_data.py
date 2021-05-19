import pandas as pd
from sqlalchemy.orm import Session

from app.models.production_data import Shift_production_data,Equip_production_data,Personnel_production_data,Welding_workers

class CRUDProduction_data:
    def get_list_personnel_production_data(self, db: Session):
        return db.query(Personnel_production_data).all()
    def get_list_shift_production_data(self, db: Session):
        return db.query(Shift_production_data).all()
    def get_list_equip_production_data(self, db: Session):
        return db.query(Equip_production_data).all()
    def get_list_welding_workers(self, db: Session):
        return db.query(Welding_workers).all()
    def down_welding_workers(self, db: Session):
        item_lists = self.get_list_welding_workers(db=db)
        item_lists_dict = [i.dobule_to_dict() for i in item_lists]
        print(item_lists_dict)
        pd.DataFrame(item_lists_dict).to_csv('welding_workers.csv')
        return True
    def down_shift_production_data(self, db: Session):
        item_lists = self.get_list_shift_production_data(db=db)
        item_lists_dict = [i.dobule_to_dict() for i in item_lists]
        print(item_lists_dict)
        # with open('/app/file/welding_equipment.csv','wb') as f:
        #     pass
        pd.DataFrame(item_lists_dict).to_csv('shift_production_data.csv')
        return True
    def down_personnel_production_data(self, db: Session):
        item_lists = self.get_list_personnel_production_data(db=db)
        item_lists_dict = [i.dobule_to_dict() for i in item_lists]
        print(item_lists_dict)
        # with open('/app/file/welding_equipment.csv','wb') as f:
        #     pass
        pd.DataFrame(item_lists_dict).to_csv('personnel_production_data.csv')
        return True
    def down_equip_production_data(self, db: Session):
        item_lists = self.get_list_equip_production_data(db=db)
        item_lists_dict = [i.dobule_to_dict() for i in item_lists]
        print(item_lists_dict)
        # with open('/app/file/welding_equipment.csv','wb') as f:
        #     pass
        pd.DataFrame(item_lists_dict).to_csv('equip_production_data.csv')
        return True        
    
curd_production_data = CRUDProduction_data()
