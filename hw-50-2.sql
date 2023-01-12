--добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)
ALTER TABLE products ADD CONSTRAINT chk_products_unit_price CHECK (unit_price > 0);

--добавить ограничение, что поле discontinued таблицы products может содержать только значения 0 или 1
ALTER TABLE products ADD CONSTRAINT chk_products_discontinued CHECK (discontinued IN (0, 1));

--Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)
SELECT * INTO discontinued_products
FROM products
WHERE discontinued = 1;

--Удалить из products товары, снятые с продажи (discontinued = 1)
SET session_replication_role = 'replica';
DELETE FROM products
WHERE discontinued = 1
SET session_replication_role = 'origin';