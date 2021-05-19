"""

生产设备管理模块

"""
from datetime import date
from sqlalchemy import Column, Integer, String, VARCHAR, Text, Date

from app.db.base_class import Base



class Shift_production_data(Base):
    """
    
    班组生产数据
    """
    __tablename__ = "shift_production_data"
    id = Column(Integer, primary_key=True, index=True)
    team_id =  Column(VARCHAR(255), primary_key=True,index=True, nullable=True, comment="所属班组")
    equipment_sum = Column(VARCHAR(255), nullable=True, comment="设备总数")
    start_up_sum = Column(VARCHAR(255), nullable=True, comment="开机设备数")
    welding_sum = Column(VARCHAR(255), nullable=True, comment="实焊设备数")
    welding_time = Column(VARCHAR(255), nullable=True, comment="焊接时间")
    working_time = Column(VARCHAR(255), nullable=True, comment="工作时间")

class Equip_production_data(Base):
    """
    
    设备生产数据 
    """
    __tablename__ = "equip_production_data"
    id = Column(Integer, primary_key=True, index=True)
    team_id =  Column(VARCHAR(255), primary_key=True, index=True, nullable=True, comment="所属班组")
    equipment_id  = Column(VARCHAR(255), nullable=True, comment="设备总数")
    start_up_sum = Column(VARCHAR(255), nullable=True, comment="开机设备数")
    welding_sum = Column(VARCHAR(255), nullable=True, comment="实焊设备数")
    welding_time = Column(VARCHAR(255), nullable=True, comment="焊接时间")
    working_time = Column(VARCHAR(255), nullable=True, comment="工作时间")
    welding_efficiency = Column(VARCHAR(255), nullable=True, comment="焊接效率")


class Personnel_production_data(Base):
    """
    
    人员生产数据 
    """
    __tablename__ = "personnel_production_data"
    id = Column(Integer, primary_key=True, index=True)
    welder_id =  Column(VARCHAR(255), primary_key=True,  index=True, nullable=True, comment="焊工编号")
    welder_name = Column(VARCHAR(255), nullable=True, comment="焊工名称")
    welding_time = Column(VARCHAR(255), nullable=True, comment="焊接时间")
    working_time = Column(VARCHAR(255), nullable=True, comment="工作时间")
    welding_efficiency = Column(VARCHAR(255), nullable=True, comment="焊接效率")

class Welding_workers(Base):
    """
    
    人员生产数据 
    """
    __tablename__ = "welding_workers"
    id = Column(Integer, primary_key=True, index=True)
    equip_id = Column(Integer, nullable=True,index=True)
    welding_pid =  Column(Integer, primary_key=True,  index=True, nullable=True, comment="焊工编号")
    wlding_name = Column(VARCHAR(255), nullable=True, comment="焊工名称")
    bto_group_number = Column(VARCHAR(255), nullable=True, comment="焊接时间")
    work_status = Column(VARCHAR(255), nullable=True, comment="工作时间")
