# # -------------пример с бд Сотрудники--------------- #
# import sqlite3
#
# # Устанавливаем соединение с базой данных
# conn = sqlite3.connect('Company.db') # указываем путь где есть БД или где будет созадана
#
# # Создаем курсор для выполнения SQL-запросов
# cursor = conn.cursor()
#
# # Создаем таблицу
# cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
#                         id INTEGER PRIMARY KEY,
#                         name TEXT,
#                         position TEXT,
#                         salary REAL)''')
#
# # # Вставляем данные в таблицу
# # cursor.executescript('''
# # INSERT INTO employees (name, position, salary)
# # VALUES
# # ('John Doe', 'HR Manager', 5000),
# # ('Jane Smith', 'HR Assistant', 3500);''')
#
# # Сохраняем изменения
# # conn.commit()
#
# # Выполняем запрос, который нас интересует
# cursor.execute("SELECT * FROM employees")
#
# # Получаем результаты запроса
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# # закрываем соединение
# conn.close()




# ---------------пример по работе с БД Магазин---------------------- #

'''
создать БД
создать таблицу в бд
наполнить таблицу записями
Код для работы с запросами select 
'''
