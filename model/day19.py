from typing import Optional

from sqlmodel import Field

from . import BaseModel


class Lrc(BaseModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    day: int
    st: int
    en: str
    zh: str
    start: int
