"""
    @author: Jedore
    @project: ToeicBackend
    @file: __init__.py.py
    @time: 2022/11/28 21:35
    @desc:
"""
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Rsp(SQLModel):
    code: int = Field(0)
    msg: str = Field('')


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


class Base(SQLModel):
    t_created: datetime
    t_updated: datetime
    t_deleted: datetime


