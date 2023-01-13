--уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
--Написать запрос именно с использвованием подзапроса.
SELECT DISTINCT product_name
FROM products
WHERE product_id IN(
	SELECT product_id
	FROM order_details
	WHERE quantity=10);