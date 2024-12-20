def dogs_age(age: int | float) -> int | float | str:
    return age * 10.5 if 0 < age <= 2 else 21 + (age - 2) * 4 if age >2 else f'age must be greater than 0'


def dogs_age_2(age: int| float) -> int | float:
    if not isinstance(age, (int, float)) or type(age) is bool:
        raise TypeError(f'Expected int or float but got {type(age)}')
    if age <= 0:
        raise ValueError('age must be greater than 0')
    return age * 10.5 if age <= 2 else 21 + (age - 2) * 4

# print(dogs_age(10))
# print(dogs_age(1.5))
# print(dogs_age(0))
print(dogs_age_2(-1))