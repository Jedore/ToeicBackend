"""
    @author: Jedore
    @project: ToeicBackend
    @file: exceptions.py
    @time: 2022/11/27 21:40
    @desc:
"""


class TException(Exception):
    ...


class AuthException(TException):
    ...


class ParamException(TException):
    ...


handlers = {}
