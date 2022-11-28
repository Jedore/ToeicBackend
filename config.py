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

DB_URL = getenv('DB_URL')
DB_URL = f'postgresql+pyscopg2://{DB_URL}'
