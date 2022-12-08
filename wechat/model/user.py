"""
    @author: Jedore
    @project: ToeicBackend
    @file: user.py
    @time: 2022/12/7 21:14
    @desc:
"""
from sqlmodel import Field, SQLModel

from model import BaseModel


class User(SQLModel):
    openid: str = Field(primary_key=True, alias='openId')
    union_id: str = Field(alias='unionId')
    gender: str
    nickname: str = Field(alias='nickName')
    avatar_url: str = Field(alias='avatarUrl')
    country: str
    province: str
    city: str
    session_key: str


class UserDB(User, BaseModel, table=True):
    ...
