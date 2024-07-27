from config import *

def add_client(name, birth_date, email, phone_number):
    with sqlite3.connect('shop.db') as con:  # установка соединения
        cursor = con.cursor()

        cursor.executescript(f'''INSERT INTO clients (name, birth_date, email, phone_number) VALUES
        ('{name}', '{birth_date}', '{email}', '{phone_number}');
        ''')

def show_client(name: str='', birth_date: str = '', email: str='', phone_number: str=''):
    with sqlite3.connect('shop.db') as con:  # установка соединения
        cursor = con.cursor()

        script = f'''SELECT * FROM Clients WHERE true'''
        if name != '':
            script += f' AND name = "{name}" '
        if birth_date != '':
            script += f' AND birth_date = "{birth_date}" '
        if email != '':
            script += f' AND email = "{email}" '
        if phone_number != '':
            script += f' AND phone_number = "{phone_number}" '
        script += ';'

        cursor.execute(script)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def edit_client(id: int, name: str = '', birth_date: str = ''):
    with sqlite3.connect('shop.db') as con:  # установка соединения
        cursor = con.cursor()
        if name != '':
            cursor.execute(f''' UPDATE Clients
                                SET name = '{name}'
                                WHERE id = {id};''')
        if birth_date != '':
            cursor.execute(f''' UPDATE Clients
                                SET birth_date = '{birth_date}'
                                WHERE id = {id};''')
        con.commit()

# не удаляется клиент
def delete_client(id):
    with sqlite3.connect('shop.db') as con:  # установка соединения
        cursor = con.cursor()
        cursor.execute(f'''DELETE FROM Clients WHERE id = {id};''')
        con.commit()
