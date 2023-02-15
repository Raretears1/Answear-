import sqlite3 as sq

import allure

from playwright_test.utils import add_to_db


# *********************************** CONNECT TO DB ***********************************
@allure.step
def connect_to_db(db_gender):
    with sq.connect('connect_to_db/answear.db') as con:
        cur = con.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS orders (
            Gender TEXT,
            Item TEXT,
            Price INTEGER,
            Total_price INTEGER     
            )''')

        print(f'self : {db_gender}')
        cur.execute(
            f"INSERT INTO orders (Gender, Item, Price, Total_price) VALUES ({add_to_db.get(f'{db_gender}')})")

