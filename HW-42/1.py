'''
1 задание
'''
import re

def to_camel_case(text):
    return re.split('_|-', text)[0] + ''.join(word.title() for word in re.split('_|-', text)[1::])


'''
2 задание
'''

class SingletonMeta(type):

    _instances = {}
    def __str__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(args, kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


'''
3 задание
'''

count_bits = lambda n: bin(n).count('1')


'''
4 задание
'''
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))

'''
5 задание
'''
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"