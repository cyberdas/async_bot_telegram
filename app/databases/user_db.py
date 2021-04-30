from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Table

from databases.base import BaseModel


class UsersModel(BaseModel):
    """
    Таблица пользователей бота
    """
    __tablename__ = "users"

    def __init__(self, conn):
        super(UsersModel, self).__init__(conn)

    clients = Table(
        "clients",
        BaseModel.metadata,
        Column("id", Integer, autoincrement=True, primary_key=True),
        Column("vacancy", String(100)),
        Column("region", String(100)),
        Column("job_type", String()),
    )
