"""
    @author: Jedore
    @project: ToeicBackend
    @file: auth.py
    @time: 2022/12/7 21:00
    @desc:
"""

import httpx
from fastapi import APIRouter

import config
from wechat.model import auth
from utils import wechat

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/login', response_model=auth.LoginRsp)
async def login(req: auth.LoginReq):
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    params = {
        'appid': config.APP_ID,
        'secret': config.APP_SECRET,
        'js_code': req.code,
        'grant_type': 'authorization_code',
    }
    # todo 登录异常处理
    # doc: https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/login/auth.code2Session.html
    rsp = httpx.get(url, params=params)
    data = rsp.json()
    session_key = data.get('session_key')
    user_info = wechat.decrypt(req.encrypted_data, req.iv, session_key)
    # todo create user
    return auth.LoginRsp()
