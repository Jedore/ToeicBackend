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
from utils import exceptions

app = FastAPI(debug=config.DEBUG,
              title='ToeicBackend',
              version='0.1.0',
              exception_handlers=exceptions.handlers)

if __name__ == '__main__':
    host, port = config.WEB_SERVER.split(':')
    uvicorn.run(app,
                host=host,
                port=port,
                loop='uvloop')
