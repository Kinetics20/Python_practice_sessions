def first_fn():
    x = 42

    def second_fn():
        return f'Answer for all questions : {x}'

    return second_fn


result = first_fn()
result_2 = result()
print(result())


