import datetime

class Task:
    content = ''
    date = None

    def __init__(self, content):
        self.content = content
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f'{self.content} (создано {self.date})'

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.content == other.content

    def __hash__(self):
        return hash(self.content)

    def __bool__(self):
        return bool(self.content)


class TodoList:

    def __init__(self):
        self.tasks = [None]*2

    def __setitem__(self, key, value):
        self.tasks[key] = value

    def __getitem__(self, item):
        return self.tasks[item]

    def __repr__(self):
        return str(self.tasks)

    def __delitem__(self, key):
        del self.tasks[key]

    def __iter__(self):
        self.value = -1
        return self

    def __next__(self):
        if self.value + 1 < len(self.tasks):
            self.value += 1
            return self.tasks[self.value]
        else:
            raise StopIteration


todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')

for item in todo_list: print(item)