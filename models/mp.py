"""
    @author: Jedore
    @project: ToeicBackend
    @file: mp.py
    @time: 2022/12/7 21:07
    @desc:
"""

from sqlmodel import Field, SQLModel

from . import Rsp
from .user import User


class LoginReq(SQLModel):
    code: str = Field(min_length=1, max_length=64)


class LoginRsp(Rsp):
    data: User
