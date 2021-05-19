from typing import Optional

from pydantic import  EmailStr, AnyHttpUrl
from .base import Base
from sqlalchemy.sql.functions import user


# Shared properties
class UserBase(Base):
    # email: Optional[EmailStr] = None
    username: Optional[str] = None
    phone: int = None 
    is_active: Optional[bool] = True


class UserAuth(Base):
    password: str


# 邮箱登录认证 验证数据字段都叫username
class UserEmailAuth(UserAuth):
    username: EmailStr

class UserNameAuth(UserAuth):
    username: str
    # password: str
# 手机号登录认证 验证数据字段都叫username
class UserPhoneAuth(UserAuth):
    username: int


# 创建账号需要验证的条件
class UserCreate(UserBase):
    nickname: str 
    # email: EmailStr
    username: str = 'admin'
    password: str = '123456'
    role_id: int
    avatar: 'AnyHttpUrl' = 'https://dss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/qrcode/qrcode@2x-daf987ad02.png'


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    hashed_password: str


# 返回的用户信息
class UserInfo(Base):
    role: str
    username: str
