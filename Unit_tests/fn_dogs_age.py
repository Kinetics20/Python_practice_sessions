def dogs_age(age: int | float) -> int | float | str:
    return age * 10.5 if 0 < age <= 2 else 21 + (age - 2) * 4 if age >2 else f'age must be greater than 0'




# print(dogs_age(10))
# print(dogs_age(1.5))
# print(dogs_age(0))
print(dogs_age(-1))