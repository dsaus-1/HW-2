import csv
import psycopg2
from itertools import chain

class Added_bd_table:
    _database = 'north'
    table_name = 'customers'
    file_name = ''
    number_columns = 3
    execute_first_arg = f"INSERT INTO {table_name} VALUES (%s, %s, %s)"


    def __init__(self, password: str):
        self.password = password

    def add_data(self):
        with psycopg2.connect(host='localhost', database=self._database, user='postgres', password=self.password) as conn:
            with conn.cursor() as cur:
                with open(self.file_name) as file:
                    reader_file = csv.reader(file)
                    count = 0
                    for line in reader_file:
                        if count == 0:
                            count += 1
                            continue
                        print(line)
                        cur.execute(self.execute_first_arg, tuple(chain([line[n] for n in range(self.number_columns)])))

        conn.close()


    def print_bd(self):
        with psycopg2.connect(host='localhost', database=self._database, user='postgres',
                              password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {self.table_name}")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
        conn.close()


class Customers_add(Added_bd_table):
    table_name = 'customers'
    file_name = 'customers_data.csv'
    number_columns = 3
    execute_first_arg = f"INSERT INTO {table_name} VALUES (%s, %s, %s)"


class Employees_add(Added_bd_table):
    table_name = 'employees'
    file_name = 'employees_data.csv'
    number_columns = 5
    execute_first_arg = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s)"


class Orders_add(Added_bd_table):
    table_name = 'orders'
    file_name = 'orders_data.csv'
    number_columns = 5
    execute_first_arg = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s)"



customers = Customers_add('14597')
customers.add_data()
customers.print_bd()

employees = Employees_add('14597')
employees.add_data()
employees.print_bd()

orders = Orders_add('14597')
orders.add_data()
orders.print_bd()

