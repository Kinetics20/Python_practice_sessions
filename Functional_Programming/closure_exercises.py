# create generator numbers from 1 do infinity with step = 1
from time import sleep


def outer_fn():
    index = 1

    def inner_fn():
        nonlocal index
        result = index
        index += 1
        return result
        # return index
    return inner_fn

# c = outer_fn()
# print(c())
# print(c())
# print(c())

# add possibility definition of start from counting
def outer_fn_1(index=1):


    def inner_fn():
        nonlocal index
        result = index
        index += 1
        return result
        # return index
    return inner_fn

# d = outer_fn_1(100)
# print(d())
# print(d())
# print(d())

# add possibility change numeration during execution inner function
def outer_fn_2(index=1):


    def inner_fn(new_index=None):
        nonlocal index
        if new_index is not None:
            index = new_index
        result = index
        index += 1
        return result
        # return index
    return inner_fn

# e = outer_fn_2(100)
# print(e())
# print(e(30))
# print(e(30000))
# print(e())

# nonlocal and global are not the best practice , change function and remove nonlocal from inner function

def outer_fn_3(index=1):


    def inner_fn(new_index=None):

        if new_index is not None:
            inner_fn.index = new_index
        result = inner_fn.index
        inner_fn.index += 1

        return result
    inner_fn.index = index
        # return index
    return inner_fn

e = outer_fn_3(100)
# print(e())
# print(e(30))
# print(e(30000))
# print(e())

# create function will divide or multiply depending on the first element of collection

# coll[0] >= 0 => multiply by 2
# coll[0] <  0 => divide   by 2


def calculate():

    predicate = None
    def inner(item):
        nonlocal predicate

        if predicate is None:
            predicate = item >= 0

        if predicate:
            return item * 2
        return item / 2

    return inner

# calc = calculate()

# r1 = list(map(calc, [1, 2, 3, 4]))
r1 = list(map(calculate(), [1, 2, 3, 4]))
# r2 = list(map(calc, [-1, 2, 3, 4]))
r2 = list(map(calculate(), [-1, 2, 3, 4]))

# print(r1, r2)

# memoizing level - 1
# memoizing - memorizing the result of a function to memory, to reuse it and avoid calculation again
# Rules :
# - fn has to be pure
# - small amount of parameters combinations

def memoize():
    cache = {}
    print('outer')

    def inner(a, b):
        print('inner')
        key = f'{a},{b}'
        if key not in cache:
            # intensive CPU task
            sleep(3)
            cache[key] = a + b
        return cache[key]

    return inner


# def calculate_magic(a, b):
#     # intensive CPU task
#     sleep(3)
#     return a + b
calculate_magic = memoize()

print(calculate_magic(1, 2))
print(calculate_magic(2, 2))
print(calculate_magic(1, 2))
print(calculate_magic(2, 2))