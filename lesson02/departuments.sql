-- https://anastasiyas-organization-2.gitbook.io/teoriya-baz-dannykh-1/v/praktika/mnogotablichnye-zaprosy/tablicy-dlya-ucheta-zadach-v-proekte-i-naznacheniya-sotrudnikov-na-eti-zadachi.
-- Создаем таблицу departments
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

-- Создаем таблицу employees с внешним ключом department_id
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department_id INTEGER,
    position TEXT,
    salary REAL,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
-- Создаем таблицу проектов
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    description TEXT
);

-- Создаем таблицу задач
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER,
    name TEXT,
    description TEXT,
    status TEXT,
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Создаем таблицу, связывающую сотрудников с задачами
CREATE TABLE IF NOT EXISTS employee_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    task_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES employees(id),
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);

--1. Получить все задачи для конкретного проекта.
SELECT t.name AS 'Задачи для проекта'
FROM tasks t
JOIN projects p ON t.project_id = p.id
WHERE p.name = 'Project A';

--2. Получить список всех задач, назначенных определенному сотруднику.
SELECT e.name, t.name AS 'Задачи для сотрудника'
FROM tasks t
JOIN employee_tasks et ON et.task_id = t.id
JOIN employees e ON et.employee_id = e.id
WHERE e.name = 'John Doe';


--3. Получить список всех задач, которые еще не назначены на сотрудников.
SELECT t.name AS 'Не назначенные задачи'
FROM tasks t
left JOIN employee_tasks et ON et.task_id = t.id
left JOIN employees e ON et.employee_id = e.id 
where et.employee_id is NULL;


--6. Получить список всех сотрудников и количество задач, назначенных каждому из них.
SELECT COUNT(description) as 'Количество задач',e.name
FROM tasks t
JOIN employee_tasks et ON t.id = et.task_id
JOIN employees e ON e.id = et.employee_id
GROUP BY e.id;

-- 8. Получить список всех сотрудников, назначенных на задачи в проекте.
select distinct employees.name, projects.name from employees
join employee_tasks on employee_tasks.employee_id = employees.id
join tasks on employee_tasks.task_id = tasks.id
join projects on tasks.project_id = projects.id;



 
--10. Получить общее количество задач, завершенных в каждом проекте.
SELECT COUNT(t.description), p.name
FROM projects p
JOIN tasks t ON p.id = t.project_id 
where t.status = 'Completed'
group by p.id;








