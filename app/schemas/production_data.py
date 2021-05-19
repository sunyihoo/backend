from .base import Base


class Shift_production_data(Base):
    """
    
    班组生产数据
    """
    id: int = None
    team_id: str = None
    equipment_sum: str = None
    start_up_sum: str = None
    welding_sum: str = None 
    welding_time: str = None
    working_time: str = None

class Equip_production_data(Base):
    id : int = None
    team_id : str = None
    equipment_id: str = None
    start_up_sum: str = None
    welding_sum: str = None
    welding_time: str = None
    welding_efficiency: str = None


class Personnel_production_data(Base):
    """
    
    人员生产数据 
    """
    id: int = None
    welder_id: str = None
    welder_name: str = None
    welding_time: str = None
    working_time: str = None
    welding_efficiency: str = None
