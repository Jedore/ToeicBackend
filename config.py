"""
    @author: Jedore
    @project: ToeicBackend
    @file: config.py
    @time: 2022/11/27 21:39
    @desc:
"""
from os import getenv

DEBUG = getenv('DEBUG') == 'True'

WEB_SERVER = getenv('WEB_SERVER', '127.0.0.1:8000')
