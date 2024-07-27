from config import *

def add_product(product_name, price, category):
    with sqlite3.connect('shop.db') as con:  # установка соединения
        cursor = con.cursor()

        cursor.executescript(f'''INSERT INTO Products (product_name, price, category) VALUES
        ('{product_name}', {price}, '{category}');
        ''')

def show_products():
    with sqlite3.connect('shop.db') as con:  # установка соединения
        cursor = con.cursor()

        cursor.execute(f'''
        SELECT * FROM Products
        ''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)