from .base import BaseModel

class Shift_welding(BaseModel):
    """
    
    班组焊接数据
    """
    id: int = None
    team_id: str = None
    equipment_sum: str = None
    start_up_sum: str = None
    welding_sum: str = None
    welding_time: str = None
    working_time: str = None

class Equip_welding(BaseModel):
    """
    
    设备焊接数据 
    """
    id : int = None
    team_id: str = None
    start_up_sum: str = None
    welding_sum : str = None
    welding_time: str = None
    welding_efficiency: str = None


class Personnel_welding(BaseModel):
    """
    
    人员焊接数据 
    """
    id: int = None
    personnel_id: str = None
    personnel_name: str = None
    personnel_accumulated_welding_time: str = None
    normal_duration: str = None
