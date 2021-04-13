import asyncio
import aiosqlite
import sqlite3
import os
import logging


class AsyncDataBase:
    
    def __init__(self, name):
        self.name = name
        self._connection = self.connect()

    def create_db(self, db_name):
        with sqlite3.connect(f"{self.name}.db") as db:
            db.execute('''CREATE TABLE users_search 
                        (user_id INTEGER,
                        search VARCHAR NOT NULL);''')
            logging.info("Таблица создана")

    def connect(self):
        dp_path = os.path.join(os.getcwd(), f"{self.name}.db")
        if not os.path.exists(dp_path):
            self.create_db(self.name)
        return sqlite3.connect(f"{self.name}.db")

    async def add_search_results(self, user_id, search_results):
        sql = f"""INSERT INTO users_search (id, search)
                VALUES ({user_id}, {search_results});"""
        with self._connection as db:
            cursor =  await db.execute(sql)
            await db.commit()
            rows = await curcor.fetchall()
            print(rows)

    async def search(self, user_id):
        sql = """SELECT * FROM users_search;"""
        async with aiosqlite.connect(f"{self.name}.db") as db:
            cursor = db.execute(sql)
            print(cursor.fetchall())

#async def add_search_results(user_id, search_results):
 #   sql = f"""INSERT INTO users_search (user_id, search)
   #         VALUES ({user_id}, {search_results});"""
   # async with aiosqlite.connect("users_search.db") as db:
       # cursor =  await db.execute(sql)
       # await db.commit()
        #rows = await cursor.fetchall()
        #print(rows)
# return connection
#async def count_search_results(user_id):
    #sql = f"""SELECT * FROM users_search WHERE user_id = {user_id}""" 



# user_db = AsyncDataBase("users_search")
#async def test_func():
    #task = asyncio.create_task(add_search_results(123123, "123"))
    ##task1 = asyncio.create_task(count_search_results(123123))
    #await task
    # await task1


#loop = asyncio.get_event_loop()
# loop.run_until_complete(test_func())
# user_db.connect()
# sql_command = """INSERT INTO users_search (123, kqw[ppwqe]);"""
# user_db.add_search_results()
# db.connect()

# async def create_db():
    #async with aiosqlite.connect()