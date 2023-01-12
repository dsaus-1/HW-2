-- Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student
(
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
);

--Добавить в таблицу после создания колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar;

--Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name;

--Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME birthday TO birth_date;

--Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student ALTER COLUMN phone SET DATA TYPE varchar(32);

--Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, birth_date)
VALUES ('Harry', 'Potter', '1990-02-02');
INSERT INTO student (first_name, last_name, birth_date)
VALUES ('Harry2', 'Potter2', '1990-03-03');
INSERT INTO student (first_name, last_name, birth_date)
VALUES ('Harry3', 'Potter3', '1990-04-04');

--Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student RESTART IDENTITY;