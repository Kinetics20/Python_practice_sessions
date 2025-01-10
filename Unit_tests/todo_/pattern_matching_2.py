# Pattern matching

# TODO 1// simple match

def ex_1():
    while True:
        command = input('Enter command: \n')
        match command:
            case 'add todo':
                print(f'ToDo added!')
            case 'show todo':
                print('Yours todos')
            case 'bye':
                print('Bye!')
                break
            # TODO case _ - when the user enter invalid input not matched to the case
            # wild card !!!!
            case _:
                print('unknown command')


# ex_1()


# TODO 2// match on different types


def ex_2():
    for x in 1, 'two', 3.14, Exception('home'), lambda data: data + 42:
        match x:
            case int():
                print(f'int: {x}')
            case str():
                print(f'str: {x}')
            case float():
                print(f'float: {x}')
            case Exception():
                print(f'Exception: {x}')
            case y:
                print(f'y: {y}')


# ex_2()


# TODO 3// guarded matching


def ex_3():
    for i in range(6):
        match i:
            # guard - condition - if i < 4
            case 1 | 3 | 5 if i < 4:
                print(f'{i} is odd and less than 4')
            case 1 | 3 | 5 if i > 4:
                print(f'{i} is odd and greater than 4')
            case 2 | 4:
                print(f'{i} is even')


ex_3()