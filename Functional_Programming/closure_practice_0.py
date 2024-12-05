def add(a, b):
    return a + b

print(add(1, 2))
add.sth = 4200
add.sth_2 = 'Home'

print(add.sth)
print(add.sth_2)
print(add(1, 2))

add.add = add
print(add.add.add.add.add.add.add(3, 3))

