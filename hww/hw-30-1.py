import datetime

'''
то, что у меня выдает сначала "Выйти на пробежку" и "Выпить кофе",
а только потом 'Сделать домашку', это ок или должно выводить как в задании сначала 'Сделать домашку'?
'''
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

# todo_list = set()
#
# todo_list.add(Task('Сделать домашку'))
# todo_list.add(Task('Выпить кофе'))
# todo_list.add(Task('Выйти на пробежку'))
# todo_list.add(Task('Сделать домашку'))
#
# for item in todo_list:
#     print(item)

