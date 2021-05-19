from typing import Optional

from .base import Base


class Token(Base):
    access_token: str
    token_type: str


class TokenPayload(Base):
    sub: Optional[int] = None
