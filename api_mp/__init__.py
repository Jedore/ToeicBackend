"""
    @author: Jedore
    @project: ToeicBackend
    @file: __init__.py.py
    @time: 2022/12/7 20:59
    @desc:
"""

from fastapi import APIRouter

from . import auth

router_mp = APIRouter(prefix='/wechat', tags=['WeChat'])
router_mp.include_router(auth.router)
