"""
    @author: Jedore
    @project: ToeicBackend
    @file: auth.py
    @time: 2022/12/7 21:07
    @desc:
"""

from sqlmodel import Field, SQLModel

from model import Rsp
from .user import User


class LoginReq(SQLModel):
    code: str = Field(min_length=1, max_length=64)
    encrypted_data: str = Field(title='用户加密数据', alias='encryptedData')
    iv: str = Field(title='加密算法的初始向量')


class LoginRsp(Rsp):
    ...
