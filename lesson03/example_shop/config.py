# ---------------пример по работе с БД Магазин---------------------- #

'''
создать БД
создать таблицу в бд
'''

import sqlite3

con = sqlite3.connect('shop.db')

cursor = con.cursor()

# сделать функцию на создание
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date DATE DEFAULT CURRENT_DATE,
    email TEXT DEFAULT 'example@example.com',
    phone_number TEXT NOT NULL DEFAULT '000-000-0000'
);
''')

con.close()

