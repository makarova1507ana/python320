CREATE TABLE IF NOT EXISTS clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- PRIMARY KEY - уникальность значений, для организации связи между таблицами
    name TEXT NOT NULL);
    
    
CREATE TABLE IF NOT EXISTS phones(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER UNIQUE NOT NULL,
    id_client INTEGER,
    FOREIGN KEY(id_client) REFERENCES clients(id) -- FOREIGN KEY внешний ключ устанавливает связь с primary key с  таблицей
);

/*INSERT INTO clients (name) 
VALUES ('Иван'),
('Антон'),
('Алексей'),
('Михаил');*/

/*
INSERT INTO phones (number, id_client) VALUES 
(111111111, 1),
(111111112, 1),
(211111111, 2),
(222222222, 3),
(221111111, NULL),
(331111111, NULL);*/


SELECT COUNT(number) AS 'Свободные номера телефонов'
FROM Phones
WHERE id_client IS NULL;


SELECT number AS 'Свободные номера телефонов'
FROM Phones
WHERE id_client IS NULL