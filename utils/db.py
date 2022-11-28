"""
    @author: Jedore
    @project: ToeicBackend
    @file: db.py
    @time: 2022/11/28 23:26
    @desc:
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(config.DB_URL,
                                  pool_size=50,
                                  pool_recycle=3600,
                                  pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
DBBase = declarative_base(bind=engine, metadata=metadata)
