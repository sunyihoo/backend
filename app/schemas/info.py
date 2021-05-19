from .base import Base
from typing import List

class Info(Base):
    password: str
    roles: List
    token: str
    introduction: str
    avatar: str
    name: str