-- Создаем таблицу продуктов
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
);

-- Создаем таблицу заказов
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_name TEXT,
    order_date DATE
);

-- Создаем таблицу-связь элементов заказа
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Вставляем данные в таблицу products
INSERT INTO products (name, price) VALUES ('Книга', 15.99);
INSERT INTO products (name, price) VALUES ('Футболка', 29.99);
INSERT INTO products (name, price) VALUES ('Наушники', 99.99);
INSERT INTO products (name, price) VALUES ('Мышка', 19.99);
INSERT INTO products (name, price) VALUES ('Кружка', 9.99);

-- Вставляем данные в таблицу orders
INSERT INTO orders (customer_name, order_date) VALUES ('Иван Иванов', '2024-02-25');
INSERT INTO orders (customer_name, order_date) VALUES ('Мария Петрова', '2024-02-26');
INSERT INTO orders (customer_name, order_date) VALUES ('Алексей Сидоров', '2024-02-27');

-- Вставляем данные в таблицу order_items
INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 1, 2); -- 2 книги в первом заказе
INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 3, 1); -- 1 наушники в первом заказе
INSERT INTO order_items (order_id, product_id, quantity) VALUES (2, 2, 3); -- 3 футболки во втором заказе
INSERT INTO order_items (order_id, product_id, quantity) VALUES (3, 4, 1); -- 1 мышка в третьем заказе
INSERT INTO order_items (order_id, product_id, quantity) VALUES (3, 5, 4); -- 4 кружки в третьем заказе





--1.Получить список всех продуктов.
SELECT *
FROM products;
 
--2.Получить список всех заказов.
SELECT *
FROM orders;
 
--3. Получить список всех элементов заказа с указанием продукта и его цены
SELECT  name, price, quantity, customer_name, order_date
FROM products p
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON o.id = oi.order_id;
 






--4. Получить список всех элементов с именем клиента и суммой заказа (сумма всех продуктов в заказе)
SELECT customer_name, SUM(price * quantity)
FROM products p
JOIN order_items oi ON p.id = oi.product_id 
JOIN orders o ON o.id = oi.order_id
GROUP BY o.id;




--5. Получить сумму всех продаж за определенную дату
SELECT order_date, SUM(price * quantity)
FROM products p , orders o
JOIN orders ON p.id = o.id and o.order_date = '2024-02-26'



 
--6. Получить список всех продуктов, цена которых меньше 20
/*SELECT *
FROM products
WHERE price < 20*/
 
--7. Получить общее количество продуктов в каждом заказе
--SELECT SUM(quantity)
--FROM order_items
 
-- 8. Получить список заказов, сделанных после определенной даты.
SELECT customer_name, order_date, name
FROM products p, orders o
JOIN orders ON o.id = p.id and o.order_data BEFORE = '2024-02-25'
 
