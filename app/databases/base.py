from typing import List

from asyncpg import Record
from sqlalchemy import MetaData, Column, func, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    """Базовый класс для моделей"""
    __abstract__: bool = True
    __tablename__: str = None

    metadata = MetaData()

    def __init__(self, conn):
        self.conn = conn

    @property
    def name(self):
        return self.__tablename__
