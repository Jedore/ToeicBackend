"""
    @author: Jedore
    @project: ToeicBackend
    @file: main.py
    @time: 2022/11/27 21:39
    @desc:
"""
import uvicorn
from fastapi import FastAPI

import config
import wechat
from utils import exceptions

app = FastAPI(debug=config.DEBUG,
              title='ToeicBackend',
              version='0.1.0',
              exception_handlers=exceptions.handlers)

app.include_router(wechat.router)

if __name__ == '__main__':
    host, port = config.WEB_SERVER.split(':')
    uvicorn.run(app,
                host=host,
                port=int(port),
                loop='uvloop')
