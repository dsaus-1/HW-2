class Meta(type):

    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for key in attrs:
            ku = key.upper()
            new_attrs[ku] = attrs[key]

        return type.__new__(cls, name, bases, new_attrs)


class Math(metaclass=Meta):
    pi = 3.141592653589793
    e = 2.718281828459045
    tau = 6.283185307179586

m = Math()
print(m.PI)
#3.141592653589793
print(m.E)
#2.718281828459045
print(m.pi)
#AttributeError: 'Math' object has no attribute 'pi'

