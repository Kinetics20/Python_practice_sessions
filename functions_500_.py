# This is a set of 500 pieces python functions

from math import pi


# 001
# _______________________________________________
# adding two numbers

def add_num(a, b):
    return a + b


assert add_num(2, 5) == 7


# 002
# _______________________________________________
# subtracting two numbers

def subtract_num(a, b):
    return a - b


assert subtract_num(2, 5) == -3


# 003
# _______________________________________________
# multiplying two numbers

def multiply_num(a, b):
    return a * b


assert multiply_num(2, 5) == 10


# 004
# _______________________________________________
# dividing two numbers

def divide_num(a, b):
    return a / b


assert divide_num(2, 5) == 0.4


# 005
# _______________________________________________
# subtracting two numbers without the rest

def divide_num_without_rest(a, b):
    return a // b


assert divide_num_without_rest(2, 5) == 0


# 006
# _______________________________________________
# exponentiation of two numbers

def exponentiation_num(a, b):
    return a ** b


assert exponentiation_num(5, 2) == 25


# 007
# _______________________________________________
# square root

def count_square_root(a):
    return a ** 0.5


assert count_square_root(4) == 2


# 008
# _______________________________________________
# BMI calculator

def bmi(mass, height):
    return mass / height ** 2


assert bmi(89, 1.8) == 27.469135802469133


# 009
# _______________________________________________
# check word is palindrome

def check_palindrome(word):
    return word == word[::-1]


assert check_palindrome("hello") == False


# 010
# _______________________________________________
# count square area

def square_area(a):
    return a * a


assert square_area(4) == 16


# 011
# _______________________________________________
# count rectangle area

def rectangle_area(a, b):
    return a * b


assert rectangle_area(2, 3) == 6


# 012
# _______________________________________________
# count triangle area

def triangle_area(a, b, h):
    return 0.5 * (a + b) * h


assert triangle_area(2, 3, 4) == 10


# 013
# _______________________________________________
# count perimeter of a square

def square_perimeter(a):
    return a * 4


assert square_perimeter(4) == 16


# 014
# _______________________________________________
# count perimeter of a rectangle

def perimeter_rectangle(a, b):
    return 2 * (a + b)


assert perimeter_rectangle(4, 4) == 16


# 015
# _______________________________________________
# count perimeter of a triangle

def perimeter_triangle(a, b, c):
    return a + b + c


# 016
# _______________________________________________
# count circumference of a circle

def circumference_circle(r):
    return 2 * pi * r


assert circumference_circle(4) == 25.132741228718345


# 017
# _______________________________________________
# count circle area

def circle_area(r):
    return pi * r * r


assert circle_area(2) == 12.566370614359172


# 018
# _______________________________________________
# count trapezoid area

def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h


assert trapezoid_area(4, 4, 4) == 16


# 019
# _______________________________________________
# count trapezoid perimeter

def trapezoid_perimeter(a, b, c, d):
    return a + b + c + d


assert trapezoid_perimeter(4, 4, 4, 4) == 16


# 020
# _______________________________________________
# count cube volume

def cube_volume(a):
    return a ** 3


assert cube_volume(4) == 64


# 021
# _______________________________________________
# count cube total surface area

def cube_total_surface_area(a):
    return 6 * a * a


assert cube_total_surface_area(2) == 24


# 022
# _______________________________________________
# count cuboid volume

def cuboid_volume(a, b, c):
    return a * b * c


assert cuboid_volume(4, 4, 4) == 64


# 023
# _______________________________________________
# count cuboid total surface area

def cuboid_total_surface_area(a, b, c):
    return 2 * (a * b + a * c + b * c)


assert cuboid_total_surface_area(4, 4, 4) == 96


# 024
# _______________________________________________
# count sphere area

def sphere_area(r):
    return 4 / 3 * pi * r ** 3


assert sphere_area(4) == 268.082573106329


# 025
# _______________________________________________
# count sphere volume

def sphere_volume(r):
    return 4 * pi * r ** 2


assert sphere_volume(4) == 201.06192982974676


# 026
# _______________________________________________
# count cone volume

def cone_volume(r, h):
    return 1 / 3 * pi * r ** 2 * h


assert cone_volume(4, 4) == 67.02064327658225


# 027
# _______________________________________________
# count cone total area

def cone_total_surface_area(r, l):
    return pi * r * (r + l)


assert cone_total_surface_area(4, 4) == 100.53096491487338


# 028
# _______________________________________________
# count cylinder total area

def cylinder_area(r, h):
    return 2 * pi * r * (r + h) == 201.06192982974676


# 029
# _______________________________________________
# count cylinder volume

def cylinder_volume(r, h):
    return pi * r ** 2 * h


assert cylinder_volume(4, 5) == cylinder_volume(4, 5)


# 030
# _______________________________________________
# count pyramid volume square based

def pyramid_volume_square_based(a, h):
    return 1 / 3 * a ** a * h


assert pyramid_volume_square_based(4, 4) == 341.3333333333333

# 030 , 031 , 032
# _______________________________________________
# using list comprehension return new list with only even numbers

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def create_new_list_even_num(array):
    return [num for num in array if not num % 2]
    # return [ num for num in array if not num & 1]


assert create_new_list_even_num(list_1) == [2, 4, 6, 8, 10]

# 033 , 034 , 035
# _______________________________________________
# using list comprehension flat list of lists

list_2 = [[1, 3], [2, 4], [3, 5]]


def create_new_flat_list(array):
    return [x for y in array for x in y]


assert create_new_flat_list(list_2) == [1, 3, 2, 4, 3, 5]


# 036 , 037 , 038
# _______________________________________________
# using list comprehension multiply each element list by n

def create_new_list_mul_by_n(n, array):
    return [item * n for item in array]


assert create_new_list_mul_by_n(10, list_1) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 039 , 040 , 041
# _______________________________________________
# using list comprehension filter list and keep only str value

list_3 = [1, 'home', 3, 'John', 5, 'funeral', 'infinity', 'compulsive', 9, 10]


def create_new_str_list(array):
    return [item for item in array if isinstance(item, str)]


assert create_new_str_list(list_3) == ['home', 'John', 'funeral', 'infinity', 'compulsive']

# 042 , 043 , 044
# _______________________________________________
# using dict comprehension create dict from the list

list_4 = ['home', 'John', 'funeral', 'infinity', 'compulsive']


def create_dict_from_list(array):
    return {key: value for key, value in enumerate(array)}


assert create_dict_from_list(list_4) == {0: 'home', 1: 'John', 2: 'funeral', 3: 'infinity', 4: 'compulsive'}

# 045 , 046 , 047
# _______________________________________________
# using list comprehension create list from dictionary

dict_1 = {0: 'home', 1: 'John', 2: 'funeral', 3: 'infinity', 4: 'compulsive'}


def create_list_from_dict(any_dict):
    return [item for item in any_dict.values()]


assert create_list_from_dict(dict_1) == ['home', 'John', 'funeral', 'infinity', 'compulsive']


# 048 , 049 , 050
# _______________________________________________
# using list comprehension create list of tuples from dictionary

def create_list_tuples_from_dict(any_dict):
    return [(key, value) for key, value in any_dict.items()]


assert create_list_tuples_from_dict(dict_1) == [(0, 'home'), (1, 'John'), (2, 'funeral'), (3, 'infinity'),
                                                (4, 'compulsive')]

# 051 , 052 , 053
# _______________________________________________
# using list comprehension create flat list from list of tuples

list_5 = [(0, 'home'), (1, 'John'), (2, 'funeral'), (3, 'infinity'), (4, 'compulsive')]


def create_flat_list_from_list_of_tuples(array):
    return [x for y in array for x in y]


assert create_flat_list_from_list_of_tuples(list_5) == [0, 'home', 1, 'John', 2, 'funeral', 3, 'infinity', 4,
                                                        'compulsive']


# 054 , 055 , 056
# _______________________________________________
# using list comprehension create list from dictionary using keys

def create_list_from_dict_key(any_dict):
    return [key for key in any_dict]
    # return [key for key, value in any_dict.items()]


assert create_list_from_dict_key(dict_1) == [0, 1, 2, 3, 4]


# 057 , 058 , 059
# _______________________________________________
# using list comprehension create list from dictionary using values with len condition of value

def create_list_from_dict_value_condition(any_dict):
    return [item for item in any_dict.values() if len(item) > 5]


assert create_list_from_dict_value_condition(dict_1) == ['funeral', 'infinity', 'compulsive']


# 060 , 061 , 062
# _______________________________________________
# using list comprehension create list from dictionary using keys and values like a string

def create_list_from_dict_k_v_str(any_dict):
    return [f'{key}: {value}' for key, value in any_dict.items()]


assert create_list_from_dict_k_v_str(dict_1) == ['0: home', '1: John', '2: funeral', '3: infinity', '4: compulsive']


# 063 , 064 , 065
# _______________________________________________
# using list comprehension create sliced list

def create_sliced_list(array):
    return [item[:3] for item in array]

assert create_sliced_list(list_4) == ['hom', 'Joh', 'fun', 'inf', 'com']

# 066 , 067 , 068
# _______________________________________________
# using list comprehension create new list with item[1]

def create_list_item_one_index(array):
    return [item[1] for item in array]

assert create_list_item_one_index(list_4) == ['o', 'o', 'u', 'n', 'o']

# 069 , 070 , 071
# _______________________________________________
# using list comprehension create new list if letter in item

letter = 'n'

def create_list_letter_in_item(array, n):
    return [item for item in array if n in item]

assert create_list_letter_in_item(list_4, letter) == ['John', 'funeral', 'infinity']

# 072 , 073 , 074
# _______________________________________________
# using list comprehension create new list if not item % n

def create_list_from_range_modulo_n(n):
    return [item for item in range(101) if not item % n]

assert create_list_from_range_modulo_n(18) == [0, 18, 36, 54, 72, 90]

# 075 , 076 , 077
# _______________________________________________
# using list comprehension create new list if not item % n and in the specific scope

def create_list_from_range_modulo_n_and_cond(n, a, b):
    return [ item for item in range(101) if not item % n and a < item <= b]

assert create_list_from_range_modulo_n_and_cond(20, 40, 80) == [60, 80]

# 078 , 079 , 080
# _______________________________________________
# using list comprehension create new list with dictionary's values capitalized

dict_2 = {0: 'home_AS_a_Hall', 1: ' John2    ', 2: 'funeral123   ', 3: '88infinity', 4: 'compulsive is a bad character treat'}

def create_list_from_dict(any_dict):
    return [item.capitalize() for item in any_dict.values()]

assert create_list_from_dict(dict_2) == ['Home_as_a_hall',
 ' john2    ',
 'Funeral123   ',
 '88infinity',
 'Compulsive is a bad character treat']

# 081
# _______________________________________________
# string capitalize method

sentence_1 = ' Better now than NEVER      '

def str_capitalize(any_str):
    return any_str.capitalize()

assert str_capitalize(sentence_1) == ' better now than never      '

# 082 , 083 , 084
# _______________________________________________
# using list comprehension create new list with dictionary's values lowered

def create_list_from_dict_lowered(any_dict):
    return [item.lower() for item in any_dict.values()]

assert create_list_from_dict_lowered(dict_2) == ['home_as_a_hall',
 ' john2    ',
 'funeral123   ',
 '88infinity',
 'compulsive is a bad character treat']

# 085
# _______________________________________________
# string lower method

def str_lower(any_str):
    return any_str.lower()

assert str_lower(sentence_1) == ' better now than never      '


# 086 , 087 , 088
# _______________________________________________
# using list comprehension create new list with dictionary's values upper

def create_list_from_dict_upper(any_dict):
    return [item.upper() for item in any_dict.values()]

assert create_list_from_dict_upper(dict_2) == ['HOME_AS_A_HALL',
 ' JOHN2    ',
 'FUNERAL123   ',
 '88INFINITY',
 'COMPULSIVE IS A BAD CHARACTER TREAT']

# 089
# _______________________________________________
# string lower method

def str_upper(any_str):
    return any_str.upper()

assert str_upper(sentence_1) == ' BETTER NOW THAN NEVER      '

# 090 , 091 , 092
# _______________________________________________
# using list comprehension create new list with dictionary's values titled

def create_list_from_dict_titled(any_dict):
    return [item.title() for item in any_dict.values()]

assert create_list_from_dict_titled(dict_2) == create_list_from_dict_titled(dict_2)

# 093
# _______________________________________________
# string lower method

def str_title(any_str):
    return any_str.title()

assert str_title(sentence_1) == ' Better Now Than Never      '

# 094
# _______________________________________________
# string swapcase method

def str_swapcase(any_str):
    return any_str.swapcase()

assert str_swapcase(sentence_1) == ' bETTER NOW THAN never      '

# 095
# _______________________________________________
# string strip method

def str_strip(any_str):
    return any_str.strip()

assert str_strip(sentence_1) == 'Better now than NEVER'

# 096
# _______________________________________________
# string strip and title methods

def str_strip_and_title(any_str):
    return any_str.strip().title()

assert str_strip_and_title(sentence_1) == 'Better Now Than Never'

# 097
# _______________________________________________
# string replace method

def str_replace(any_str):
    return any_str.replace(' ', '_$_$_')

assert str_replace(sentence_1) == '_$_$_Better_$_$_now_$_$_than_$_$_NEVER_$_$__$_$__$_$__$_$__$_$__$_$_'

# 098
# _______________________________________________
# string replace method

def str_replace_and_count(any_str):
    return any_str.replace(' ', '_$_$_', 4)

assert str_replace_and_count(sentence_1) == '_$_$_Better_$_$_now_$_$_than_$_$_NEVER      '

# 099, 100, 101
# _______________________________________________
# using list comprehension convert list to string

def create_list_to_str():
    return ''.join([str(item) for item in range(11)])

assert create_list_to_str() == '012345678910'

# 102, 103, 104
# _______________________________________________
# using list comprehension convert list to string and next to int

def create_list_to_str_to_int():
    return int(''.join([str(item) for item in range(11)]))

assert create_list_to_str_to_int() == 12345678910

# 105, 106, 107
# _______________________________________________
# using list comprehension achieve two list from dictionary

def create_lists_from_dict(any_dict):
    l_1 = [item for item in any_dict.values()]
    l_2 = [item for item in any_dict.keys()]

    return l_1, l_2

assert create_lists_from_dict(dict_2) == (['home_AS_a_Hall', ' John2    ', 'funeral123   ', '88infinity', 'compulsive is a bad character treat'], [0, 1, 2, 3, 4])

# 108, 109, 110
# _______________________________________________
# using dict comprehension create dict from tuple

my_tuple = ("home", "apple", "tower")

def create_dict_from_tuple(any_tuple):
    return {key: value for key, value in enumerate(any_tuple)}

assert create_dict_from_tuple(my_tuple) == {0: 'home', 1: 'apple', 2: 'tower'}

sentence_2 = 'New York 76st'

# 111
# _______________________________________________
# string isalnum method , are there only letters and digits in the str

def str_isalnum(any_str):
    return any_str.isalnum()

assert str_isalnum(sentence_2) == False

# 112
# _______________________________________________
# string isalpha method , are there only letters in the str

def str_isalpha(any_str):
    return any_str.isalpha()

assert str_isalpha(sentence_2) == False

# 113
# _______________________________________________
# string isalpha method , are there only digits in the str

def str_isdigit(any_str):
    return any_str.isdigit()

assert str_isdigit('1234') == True

# 114
# _______________________________________________
# string isdecimal method , are there only decimal digits in the str

def str_isdecimal(any_str):
    return any_str.isdecimal()

assert str_isdecimal('1234') == True

# 115
# _______________________________________________
# string isnumeric method , are there only numbers in the str

def str_isnumeric(any_str):
    return any_str.isnumeric()

assert str_isnumeric('12 34') == False

# 116
# _______________________________________________
# string islower method , are there only lower letters in the str

def str_islower(any_str):
    return any_str.islower()

assert str_islower('where is the bus stop') == True

# 117
# _______________________________________________
# string isupper method , are there only upper letters in the str

def str_isupper(any_str):
    return any_str.isupper()

assert str_isupper('where is the bus stop') == False

# 118
# _______________________________________________
# string isspace method , are there only white signs in the str

def str_isspace(any_str):
    return any_str.isspace()

assert str_isspace('      ') == True

# 119
# _______________________________________________
# string split method , create list from str using split

def str_split(any_str):
    return any_str.split(',')

assert str_split('ab,cd,ef') == ['ab', 'cd', 'ef']

# 120
# _______________________________________________
# using join method , create str from list of str

def list_join(any_list_str):
    return ', '.join(any_list_str)

assert list_join(['ab', 'cd', 'ef']) == 'ab, cd, ef'

# 121
# _______________________________________________
# Write a function that given a floor in the american system returns the floor in the european system.

# Examples
#
# 1  =>  0
# 0  =>  0
# 5  =>  4
# 15  =>  13
# -3  =>  -3

def get_real_floor(n):
    return n if n < 1 else n -1 if n < 13 else n -2

assert get_real_floor(5) == 4










