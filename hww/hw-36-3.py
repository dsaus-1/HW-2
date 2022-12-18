
class Student:

    def __init__(self, name, stud_id):
        self.name = name
        self.stud_id = stud_id
        self.lap = self.Laptop()

    def show(self):
        """Вывести информацию о студенте и его ноутбуке"""
        print(f'{self.name} {self.stud_id}\n{self.lap.name_lap} {self.lap.proc} {self.lap.ram}')

    class Laptop:
        def __init__(self):
            self.name_lap = 'HP'
            self.ram = 8
            self.proc = 'i5'


# Создаем двух студентов
s1 = Student('Ivan', 2)
s2 = Student('Mary', 3)

# Выводим данные по студенту и его нотбуку
s1.show()
# Ivan 2
# Hp i5 8

# Увеличиваем память у ноутбука студента s1
s1.lap.ram = 16
s1.show()
# Ivan 2
# Hp i5 16

# У каждого студента отдельный ноутбук (уникальный объект)
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))
# 2065309131248
# 2065309348096

