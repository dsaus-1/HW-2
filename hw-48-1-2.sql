--"имя контакта" и "город" (contact_name, country) из таблицы customers (только эти две колонки)
SELECT contact_name, country FROM customers;

--идентификатор заказа и разницу между датами формирования (order_date) заказа и его отгрузкой (shipped_date) из таблицы orders
SELECT order_id, shipped_date - order_date AS date_difference
FROM orders;

--все города без повторов, в которых зарегестрированы заказчики (customers)
SELECT DISTINCT city FROM customers;

--количество заказов (таблица orders)
SELECT COUNT(1) FROM orders;

--количество стран, в которые откружался товар (таблица orders, колонка ship_country)
SELECT COUNT(DISTINCT ship_country) FROM orders;




