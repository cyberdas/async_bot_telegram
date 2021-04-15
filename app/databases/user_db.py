import os
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine
path = os.getcwd()
#engine = create_engine(f"{path}/users.db", echo=True)
Base = declarative_base()


class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    vacancy = Column(String)  
    region = 
    job_type = 


    def __init__(self, name):

        self.name = name    


#Base.metadata.create_all(engine)
async def async_main():
    engine = create_async_engine(f"{path}/users.db", echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)

        await conn.execute(
            t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
        )

    async with engine.connect() as conn:

        # select a Result, which will be delivered with buffered
        # results
        result = await conn.execute(select(t1).where(t1.c.name == "some name 1"))

        print(result.fetchall())


asyncio.run(async_main())