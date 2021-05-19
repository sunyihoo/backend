"""

生产设备管理模块

"""
from sqlalchemy import Column, Integer, String, VARCHAR, Text
from datetime import datetime 

from app.db.base_class import Base



class Shift_welding(Base):
    """
    
    班组焊接数据
    """
    __tablename__ = "shift_welding"
    id = Column(Integer, primary_key=True, index=True)
    team_id =  Column(VARCHAR(255), nullable=True, comment="所属班组")
    accumulated_welding_time = Column(VARCHAR(255), nullable=True, comment="累计焊接时间")
    normal_duration = Column(VARCHAR(255), nullable=True, comment="正常段时长")


class Equip_welding(Base):
    """
    
    设备焊接数据 
    """
    __tablename__ = "equip_welding"
    id = Column(Integer, primary_key=True, index=True)
    team_id =  Column(VARCHAR(255), primary_key=True, index=True, nullable=True, comment="所属班组")
    equipment_id  = Column(VARCHAR(255), nullable=True, comment="设备编号")
    equip_accumulated_welding_time = Column(VARCHAR(255), nullable=True, comment="焊机累计焊接时间")
    normal_duration = Column(VARCHAR(255), nullable=True, comment="正常段时长")


class Personnel_welding(Base):
    """
    
    人员焊接数据 
    """
    __tablename__ = "personnel_welding"
    id = Column(Integer, primary_key=True, index=True)
    personnel_id =  Column(VARCHAR(255), primary_key=True, index=True, nullable=True, comment="焊工编号")
    personnel_name = Column(VARCHAR(255), nullable=True, comment="焊工名称")
    personnel_accumulated_welding_time = Column(VARCHAR(255), nullable=True, comment="焊工累计焊接时间")
    normal_duration = Column(VARCHAR(255), nullable=True, comment="正常段时长")
