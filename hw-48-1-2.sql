SELECT contact_name, country FROM customers;

SELECT order_id, shipped_date - order_date AS date_difference
FROM orders;

SELECT DISTINCT city FROM customers;

SELECT COUNT(1) FROM orders;

SELECT COUNT(DISTINCT ship_country) FROM orders;




