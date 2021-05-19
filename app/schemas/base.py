from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):
    
    start_time: Optional[datetime] =  None
    end_time: Optional[datetime] = None
    class Config:
        orm_mode = True