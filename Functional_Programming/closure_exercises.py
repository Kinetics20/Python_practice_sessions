# create generator numbers from 1 do infinity with step = 1

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
print(e())
print(e(30))
print(e(30000))
print(e())

# create function will divide or multiply depending on the first element of collection



r1 = list(map(fn, [1, 2, 3, 4]))
r2 = list(map(fn, [-1, 2, 3, 4]))

print(r1, r2)

