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

# todo_list = []
#
# todo_list.append(Task('Сделать домашку'))
# todo_list.append(Task(''))
# todo_list.append(Task('Сделать домашку'))
# todo_list.append(Task(''))
#
# non_empty_tasks = [item for item in todo_list if item]
#
# non_empty_tasks
#
# len([item for item in todo_list if not item])
