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
    colour = 'green'

    def __init__(self, model: str, max_speed: int, year: int) -> None:
        self.year = year
        self.max_speed = max_speed
        self.model = model
        self.engine = True
        # type(self).colour = new_colour
        self._colour = type(self).colour
        self.speed = 0

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)

    @classmethod
    def auto_nitro(cls, model: str, max_speed: int, year: int, nitro: bool) -> 'Auto':
        self = super().__new__(cls)
        # self = cls.__new__(cls)
        self.__init__(model, max_speed, year)
        self.nitro = nitro
        return self

    @staticmethod
    def magic():
        return 'brum!!!'

    def __len__(self) -> int:
        return 42

    # def magic(self, new_colour):
    #     type(self).colour = new_colour

    # def tune(self):
    #     self.nitro = True

doodge = Auto('Viper', 350, 2005)
porsche = Auto('911', 380, 2009)
nissan = Auto.auto_nitro('skyline',380, 2001, True)

print(nissan.nitro)

# syntactic sugar
doodge.speed_up(100)
# type(doodge).speed_up(doodge, 60)
# Auto.speed_up(doodge, 30)
print(dir(Auto))
# print(doodge.speed)

# TODO bad practice !!! declare self out of the Class !!!!!!!
# doodge.gearbox = 'Manual'

# doodge.tune()

# print(doodge.model, doodge.max_speed, doodge.year, doodge.gearbox )
# print(doodge.model, doodge.max_speed, doodge.year, doodge.nitro)
# print(doodge.model, doodge.max_speed, doodge.year, doodge.colour)
# print(doodge.model, doodge.max_speed, doodge.year)
# print(porsche.model, porsche.max_speed, porsche.year )

# TODO bad practice !!! it's possible to change class property/field but we don't apply this method
# doodge.colour = 'black'
# TODO this is write way to change class field from object level by class referring
doodge.magic = 'Gold'
# print(Auto.colour)
# print(doodge.colour)

# TODO vars is a dict with whole properties for exact object

# print(vars(Auto))
print(vars(doodge))
# print(vars(porsche))
# print(dir(doodge))
print(len(doodge))
print(doodge.__len__())



