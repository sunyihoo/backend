"""

生产设备管理模块

"""
from sqlalchemy import Column, Integer, String, VARCHAR, Text,DateTime
\
from app.db.base_class import Base



class Welding_equipment(Base):
    """
    
    焊机设备管理
    """
    __tablename__ = "welding_equipment"
    id = Column(Integer, primary_key=True, index=True)
    equip_id = Column(Integer, primary_key=True, index=True)
    ad_time = Column(DateTime, comment="入厂时间")
    type_equip = Column(VARCHAR(255), nullable=True, comment="设备类型")
    project_id = Column(VARCHAR(255), index=True, nullable=True, comment="所属项目")
    status = Column(VARCHAR(255), nullable=True, comment="状态")
    manufacturer = Column(VARCHAR(255), nullable=True, comment="厂家")
    location = Column(VARCHAR(255),  nullable=True, comment="位置")
    ip_address = Column(VARCHAR(255), index=True, nullable=True, comment="IP地址")
    equip_model = Column(VARCHAR(255), nullable=True, comment="设备型号")

class Maintain_record(Base):
    """
    
    维修记录管理 
    """
    __tablename__ = "maintain_record"
    id = Column(Integer, primary_key=True, index=True)
    equip_id = Column(Integer, index=True)
    maintain_person = Column(VARCHAR(255), index=True, nullable=True, comment="维修人员")
    start_work_time = Column(DateTime, comment="维修开始时间")
    end_work_time = Column(VARCHAR(255), nullable=True, comment="维修结束时间")
    type = Column(VARCHAR(255), index=True, nullable=True, comment="维修类型")
    description = Column(Text, nullable=True, comment="维修说明")

