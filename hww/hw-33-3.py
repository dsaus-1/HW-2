

class MyList(list):

    def __new__(cls, q):
        print('Работает магический метод')
        return super().__new__(cls)

    def __init__(self, *args):
        super().__init__(*args)
        print('Работает магический метод')

    def __str__(self):
        print('Работает магический метод')
        return super().__str__()

    def __len__(self):
        print('Работает магический метод')
        return super().__len__()

    def __setitem__(self, *args):
        print('Работает магический метод')
        super().__setitem__(*args)



lst = MyList(['Jone', 'Snow', 'Java'])


if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))



