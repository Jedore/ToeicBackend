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
from models import mp

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/login', response_model=mp.Rsp)
async def login(req: mp.LoginReq):
    url = 'https://api.weixin.qq.com/sns/jscode2session'
    params = {
        'appid': config.APP_ID,
        'secret': config.APP_SECRET,
        'js_code': req.code,
        'grant_type': 'authorization_code',
    }
    rsp = httpx.get(url, params=params)
    data = rsp.json()
    session_key = data.get('session_key')
    openid = data.get('openid')
    # todo
    return mp.Rsp()
