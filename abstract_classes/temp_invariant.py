import functools


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


def above_absolute_zero(temperature):
    return temperature._kelvin >= 0


class Temperature:
    @post_condition(above_absolute_zero)
    def __init__(self, kelvin):
        self._kelvin = kelvin

    @post_condition(above_absolute_zero)
    def get_kelvin(self):
        return self._kelvin

    @post_condition(above_absolute_zero)
    def set_kelvin(self, value):
        self._kelvin = value

    @post_condition(above_absolute_zero)
    def __repr__(self):
        return f'{type(self).__name__}(kelvin={self._kelvin})'

t = Temperature(0)

t.set_kelvin(1)