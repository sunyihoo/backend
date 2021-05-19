from datetime import datetime
from .base import Base
from typing import Optional


class Welding_equipment(Base):
    id : int = None
    equip_id: int = None
    ad_time: datetime = None
    type_equip: str = None
    project_id: str = None
    status: str = None
    manufacturer: str = None
    location: str = None
    ip_address: str = None
    equip_model: str = None

class Maintain_record(Base):
    id : int = None
    equip_id: int = None
    maintain_person: str = None
    start_work_time: datetime = None
    end_work_time: datetime = None
    type: str = None
    description: str = None
    # class Config:
    #     orm_mode = True
 