from typing import Any
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime

from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: Any
    __name__: str
    start_time = Column(DateTime,nullable=True,comment='开始时间')
    end_time = Column(DateTime,nullable=True,comment='结束时间')
    # 将表名转换为小写
    @declared_attr
    def __tablename__(cls) -> str:
        import re
        # 如果没有指定__tablename__  则默认使用model类名转换表名字
        name_list = re.findall(r"[A-Z][a-z\d]*", cls.__name__)
        # 表明格式替换成_格式 如 MallUser 替换成 mall_user
        return "_".join(name_list).lower()
        
    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result