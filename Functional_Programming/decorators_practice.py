from datetime import datetime


def reverse(fn):
    def inner(name):
        result = fn(name.swapcase())
        return result
    return inner

def upper(fn):
    def inner(name):
    # def inner(*args, **kwargs):
    #     print(f'Function {fn.__name__} was called at {datetime.now()}')
        # result = fn(*args, **kwargs)
        result = fn(name.capitalize())
        return result
        # return 'dupa'
    return inner



# @reverse
@upper
# @reverse
def say_hello(name):

    return f'Hello {name}'

@upper
def say_buy(name):

    return f'Bye {name}'


print(say_hello('jaroslaw'))
print(say_buy('Lech'))

