# ---------------пример по работе с БД Магазин---------------------- #

'''
создать БД  # config.py
создать таблицу в бд # config.py
наполнить таблицу записями
Код для работы с запросами select
'''

from client import *
from product import *





if __name__ == '__main__':
    while True:
        command = input( '''
1. Создать клиента
2. Просмотреть клиентов
3. Изменить данные клиента
4. Удалить клиента
5. Создать товар
6. Просмотреть товары
0. выйти из программы
''')
        match command:
            case '1':
                name, birth_date, email, phone_number = input('Введите имя, дату рождения(формата ГГГГ-ММ-ДД), почту, номер телефона\n').split(', ')
                add_client(name, birth_date, email, phone_number)
            #                 clients =[('Петров Петр', '1985-08-20', 'petrov@example.com', '987-654-3210'),
# ('Сидорова Елена', '1995-02-10', 'sidorova@example.com', '111-222-3333'),
# ('Смирнова Ольга', '1980-11-25', 'smirnova@example.com', '444-555-6666'),
# ('Козлова Анна', '1975-07-30', 'kozlova@example.com', '777-888-9999'),
# ('Новиков Александр', '1992-04-05', 'novikov@example.com', '000-111-2222'),
# ('Морозов Владимир', '1987-09-12', 'morozov@example.com', '333-444-5555'),
# ('Кузнецова Мария', '1998-03-20', 'kuznetsova@example.com', '666-777-8888'),
# ('Федоров Дмитрий', '1983-06-18', 'fedorov@example.com', '999-000-1111'),
# ('Алексеева Наталья', '1979-12-08', 'alekseeva@example.com', '222-333-4444')]
#                 for client in clients:
#                     add_client(*client)
            case '2':
                name = input('Введите имя\n')
                birth_date = input('Введите  дату рождения(формата ГГГГ-ММ-ДД)\n')
                email =input('Введите  почту, \n')
                phone_number = input('Введите  номер телефона\n')
                show_client(name, birth_date, email, phone_number)

            case '3':
                id = input('Введите  id\n')

                name = input('Введите имя\n')
                birth_date = input('Введите  дату рождения(формата ГГГГ-ММ-ДД)\n')

                edit_client(id, name, birth_date)
            case '4':
                id = input('Введите  id\n')
                show_client(id)

            case '5':
                product_name, price, category = input('Введите имя товара, цену, категорию\n').split(', ')
                add_product(product_name, price, category)
            case '6':
                show_products()
            case '0':
                break