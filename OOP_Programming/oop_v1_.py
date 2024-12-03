# class - namespace, (schema)
from typing import Any


# class keyword
# pascal case (upper camelspace)
# syntactic sugar


class Name:
    pass

# TODO ---> The highest class in python is object class , and always has to be in inheritance tree
# type is the highest metaclass
# params will use to execute metaclass and then metaclass will create class

# class NameTwo(object, metaclass=type, other_params='value'):
class NameTwo(object, metaclass=type):
    pass

# by metaclass
NameThree = type('NameThree', (), {})
# print(NameThree)


# by metaclass with attributes
def init_(self, x):
    self.x = x

attrs = {
    '__init__': init_,
    'value': 42
}


NameFour = type('NameFour', (object,), attrs)
nf = NameFour(777)
# print(nf.x, nf.value)

# class

class NameFive:
    def __new__(cls, *args: Any, **kwargs: Any) -> 'NameFive':
        # print(args, kwargs)
        self = super().__new__(cls)
        # self.value_ = args[0]
        return self

    def __init__(self, value):
        self.value = value
        self.temp = 42

# TODO constructor - __new__ | only object class has __new__ that can create object
# TODO constructor - after constructor ( __init__) starts __init__
# TODO MRO method resolution order - mechanism uses to search classes to provide inheritance
# TODO first __new__ create object in class, second __init__ set fields of object created by __new__
n_five = NameFive(2)
print(n_five)