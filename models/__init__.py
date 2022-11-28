"""
    @author: Jedore
    @project: ToeicBackend
    @file: __init__.py.py
    @time: 2022/11/28 21:35
    @desc:
"""

from typing import Optional

from sqlmodel import Field, SQLModel

from utils import db


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


SQLModel.metadata.create_all(db.engine)
