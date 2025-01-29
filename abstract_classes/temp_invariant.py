import functools
import inspect


def post_condition(predicate):
    def function_decorator(fn):
        @functools.wraps(fn)
        def wrapper(self, *args, **kwargs):
            result = fn(self, *args, **kwargs)
            if not predicate(self):
                r = object.__repr__(self)
                raise RuntimeError(
                    f'Post-condition {predicate.__name__} not '
                    f'maintained for {r}'
                )
            return result
        return wrapper

    return function_decorator

def invariant(predicate):
    def class_decorator(cls):
        members = list(vars(cls).items())
        for name, member in members:
            if inspect.isfunction(member):
                function_decorator = post_condition(predicate)
                decorated_member = function_decorator(member)
                setattr(cls, name, decorated_member)
        return cls

    return class_decorator

def above_absolute_zero(temperature):
    return temperature._kelvin >= 0

@invariant(above_absolute_zero)
class Temperature:

    def __init__(self, kelvin):
        self._kelvin = kelvin


    def get_kelvin(self):
        return self._kelvin


    def set_kelvin(self, value):
        self._kelvin = value


    def __repr__(self):
        return f'{type(self).__name__}(kelvin={self._kelvin})'

t = Temperature(0)

t.set_kelvin(1)