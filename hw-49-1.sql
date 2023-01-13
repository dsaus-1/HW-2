--Название компании заказчика (company_name из табл. customers) и ФИО сотрудника,
--работающего над заказом этой компании (см таблицу employees), когда и заказчик и
--сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United
--Package (company_name в табл shippers)
SELECT DISTINCT c.company_name, CONCAT(e.first_name, ' ', e.last_name) AS contact
FROM orders o
JOIN customers c USING(customer_id)
JOIN employees e USING(employee_id)
LEFT JOIN shippers s ON o.ship_via=s.shipper_id
WHERE e.city='London'
AND c.city='London'
AND s.company_name='United Package';


--Наименование продукта, количество товара (product_name и units_in_stock в табл
--products), имя поставщика и его телефон (contact_name и phone в табл suppliers) для
--таких продуктов, которые не сняты с продажи (поле discontinued) и которых меньше 25
--и которые в категориях Dairy Products и Condiments. Отсортировать результат по
--возрастанию количества оставшегося товара.
SELECT p.product_name, p.units_in_stock, s.contact_name, s.phone
FROM products p
JOIN categories c USING(category_id)
LEFT JOIN suppliers s USING(supplier_id)
WHERE p.discontinued = 0
AND p.units_in_stock < 25
AND c.category_name IN ('Dairy Products', 'Condiments')

ORDER BY p.units_in_stock


--Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
SELECT c.company_name
FROM customers c
FULL JOIN orders o USING(customer_id)
WHERE o.order_id IS NULL;
