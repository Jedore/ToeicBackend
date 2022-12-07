"""
    @author: Jedore
    @project: ToeicBackend
    @file: user.py
    @time: 2022/12/7 21:14
    @desc:
"""
from sqlmodel import Field

from . import Base


class User(Base, table=True):
    openid: str = Field(primary_key=True)
    unionid: str
