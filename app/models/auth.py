"""

用户模块

"""
from sqlalchemy import Boolean, Column, Integer, String, VARCHAR, BIGINT
from app.db.base_class import Base


class AdminUser(Base):
    """
    管理员用户表
    """
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), comment="用户昵称")
    hashed_password = Column(String(128), nullable=False, comment="密码")
    phone = Column(VARCHAR(16), unique=True, index=True, nullable=True, comment="手机号")
    role = Column(String(128),comment="角色")
    avatar = Column(String(128),comment="头像")


