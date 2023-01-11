--заказы, отправленные в города, заканчивающиеся на 'burg'. Вывести без повторений две колонки (город, страна) (см. таблица orders, колонки ship_city, ship_country)
SELECT DISTINCT ship_city, ship_country 
FROM orders
WHERE ship_city LIKE '%burg';

-- из таблицы orders идентификатор заказа, идентификатор заказчика, вес и страну отгузки. Заказ откружен в страны, начинающиеся на 'P'. Результат отсортирован по весу (по убыванию). Вывести первые 10 записей.
SELECT order_id, customer_id, freight, ship_country
FROM orders
WHERE ship_country LIKE 'P%'
ORDER BY freight DESC
LIMIT 10;

--фамилию и телефон сотрудников, у которых в данных отсутствует регион (см таблицу employees)
SELECT last_name, home_phone
FROM employees
WHERE region IS NULL;

--количество поставщиков (suppliers) в каждой из стран. Результат отсортировать по убыванию количества поставщиков в стране
SELECT country, COUNT(1) AS number_of_suppliers
FROM suppliers
GROUP BY country
ORDER BY number_of_suppliers DESC;

--суммарный вес заказов (в которых известен регион) по странам, но вывести только те результаты, где суммарный вес на страну больше 2750. Отсортировать по убыванию суммарного веса (см таблицу orders, колонки ship_region, ship_country, freight)
SELECT ship_country, SUM(freight) AS sum_on_country
FROM orders
WHERE ship_region IS NOT NULL
GROUP BY ship_country 
HAVING SUM(freight) > 2750
ORDER BY sum_on_country DESC;

--страны, в которых зарегистированы и заказчики (customers) и поставщики (suppliers) и работники (employees)
SELECT country
FROM customers
UNION
SELECT country
FROM suppliers
UNION
SELECT country
FROM employees;

--страны, в которых зарегистированы и заказчики (customers) и поставщики (suppliers), но не зарегистрированы работники (employees).
SELECT country
FROM customers
UNION
SELECT country
FROM suppliers
EXCEPT
SELECT country
FROM employees;