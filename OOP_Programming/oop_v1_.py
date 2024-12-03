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
        self.value = 'Home'
        # self.value_ = args[0]
        return self

    def __init__(self, value):
        self.value = value
        self.temp = 42

# TODO constructor - __new__ | only object class has __new__ that can create object
# TODO constructor - after constructor ( __init__) starts __init__
# TODO MRO method resolution order - mechanism uses to search classes to provide inheritance
# TODO first __new__ create object in class, second __init__ set fields of object created by __new__
# TODO metaclass type is responsible for passing params from __new__ to __init__ 
n_five = NameFive(2666)
# print(n_five.value)

# type inference - auto discovering data types

class Auto:
    def __init__(self, model: str, max_speed: int, year: int) -> None:
        self.year = year
        self.max_speed = max_speed
        self.model = model
        self.engine = True

    def tune(self):
        self.nitro = True

dodge = Auto('Viper', 350, 2005)
porsche = Auto('911', 380, 2009)
# TODO bad practice !!! declare self out of the Class !!!!!!!
dodge.gearbox = 'Manual'

dodge.tune()

# print(dodge.model, dodge.max_speed, dodge.year, dodge.gearbox )
print(dodge.model, dodge.max_speed, dodge.year, dodge.nitro)
print(porsche.model, porsche.max_speed, porsche.year )
    



