
import math


class Derivative:

    def __init__(self, func):
        self.__func = func


    def __call__(self, *args, **kwargs):
        return math.cos(*args)


# Просто считаем синус
def sin_(x):
    return math.sin(x)

print(sin_(math.pi / 3))

# 0.8660254037844386

# Считаем производную
@Derivative
def sin_(x):
    return math.sin(x)
#0.4999566978958203

print(sin_(math.pi / 3))