
class MyInt:
    def __init__(self, val):
        self.val = self.is_int(val)

    def __str__(self):
        return str(self.val)

    @classmethod
    def is_int(cls, other):
        return other if isinstance(other, int) else int(other)

    def __repr__(self):
        return f'{type(self)}: {self.val}'

    def __add__(self, other):

        return MyInt(self.val + self.is_int(other))

    def __sub__(self, other):
        return MyInt(self.val - self.is_int(other))

    def __mul__(self, other):
        return MyInt(self.val * self.is_int(other))

    def __truediv__(self, other):
        return MyInt(self.val / self.is_int(other))

