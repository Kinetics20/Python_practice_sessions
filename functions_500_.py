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
    return [item for item in range(101) if not item % n and a < item <= b]


assert create_list_from_range_modulo_n_and_cond(20, 40, 80) == [60, 80]

# 078 , 079 , 080
# _______________________________________________
# using list comprehension create new list with dictionary's values capitalized

dict_2 = {0: 'home_AS_a_Hall', 1: ' John2    ', 2: 'funeral123   ', 3: '88infinity',
          4: 'compulsive is a bad character treat'}


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


assert create_lists_from_dict(dict_2) == (
['home_AS_a_Hall', ' John2    ', 'funeral123   ', '88infinity', 'compulsive is a bad character treat'], [0, 1, 2, 3, 4])

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
    return n if n < 1 else n - 1 if n < 13 else n - 2


assert get_real_floor(5) == 4

handball_elite = [
    {
        "name": "FC Barcelona",
        "country": "Spain",
        "city": "Barcelona",
        "founded": 1942,
        "arena": "Palau Blaugrana",
        "capacity": 7500,
        "colors": ["burgundy", "navy blue"],
        "successes_in_cl": {"1st": 12, "2nd": 5, "3rd": 3},
    },
    {
        "name": "SC Magdeburg",
        "country": "Germany",
        "city": "Magdeburg",
        "founded": 1955,
        "arena": "GETEC Arena",
        "capacity": 8000,
        "colors": ["green", "red"],
        "successes_in_cl": {"1st": 4, "2nd": 0, "3rd": 0},
    },
    {
        "name": "THW Kiel",
        "country": "Germany",
        "city": "Kiel",
        "founded": 1904,
        "arena": "Sparkassen",
        "capacity": 10250,
        "colors": ["white", "black"],
        "successes_in_cl": {"1st": 4, "2nd": 4, "3rd": 3},
    },
    {
        "name": "AaB Handbold",
        "country": "Denmark",
        "city": "Aalborg",
        "founded": 2000,
        "arena": "Jutlander",
        "capacity": 5020,
        "colors": ["red", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 2, "3rd": 0},
    },
    {
        "name": "Paris SG Handball",
        "country": "France",
        "city": "Paris",
        "founded": 1941,
        "arena": "Stade Pierre",
        "capacity": 4500,
        "colors": ["blue", "red", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 1, "3rd": 4},
    },
    {
        "name": "KS Iskra Kielce",
        "country": "Poland",
        "city": "Kielce",
        "founded": 1965,
        "arena": "Hala Legionów",
        "capacity": 4200,
        "colors": ["yellow", "blue", "white"],
        "successes_in_cl": {"1st": 1, "2nd": 2, "3rd": 2},
    },
    {
        "name": "MKB Veszprem KC",
        "country": "Hungary",
        "city": "Veszprem",
        "founded": 1977,
        "arena": "Veszprém",
        "capacity": 5096,
        "colors": ["red", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 4, "3rd": 1},
    },
    {
        "name": "Fuechse Berlin",
        "country": "Germany",
        "city": "Berlin",
        "founded": 1891,
        "arena": "Max Schmeling",
        "capacity": 8500,
        "colors": ["green", "black", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "SG Flensburg-Handewitt",
        "country": "Germany",
        "city": "Flensburg-Handewitt",
        "founded": 1990,
        "arena": "Flens Arena",
        "capacity": 6300,
        "colors": ["blue", "red", "white"],
        "successes_in_cl": {"1st": 1, "2nd": 2, "3rd": 0},
    },
    {
        "name": "Sporting Clube de Portugal",
        "country": "Portugal",
        "city": "Lisbon",
        "founded": 1932,
        "arena": "Pavilhão",
        "capacity": 3000,
        "colors": ["green", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "Montpellier HB",
        "country": "France",
        "city": "Montpellier",
        "founded": 1982,
        "arena": "FDI Stadium",
        "capacity": 9000,
        "colors": ["blue", "white"],
        "successes_in_cl": {"1st": 2, "2nd": 0, "3rd": 0},
    },
    {
        "name": "Wisla Plock",
        "country": "Poland",
        "city": "Płock",
        "founded": 1964,
        "arena": "Orlen Arena",
        "capacity": 5492,
        "colors": ["blue", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "SC Pick Szeged",
        "country": "Hungary",
        "city": "Szeged",
        "founded": 1961,
        "arena": "Pick Aréna",
        "capacity": 8143,
        "colors": ["blue", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "HBC Nantes",
        "country": "France",
        "city": "Nantes",
        "founded": 1953,
        "arena": "Palais des",
        "capacity": 10750,
        "colors": ["pink", "yellow"],
        "successes_in_cl": {"1st": 0, "2nd": 1, "3rd": 0},
    },
    {
        "name": "GOG Svendborg TGI",
        "country": "Denmark",
        "city": "Gudme",
        "founded": 1973,
        "arena": "Phønix Tag",
        "capacity": 2265,
        "colors": ["yellow", "red"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "Dinamo Bucarest",
        "country": "Romania",
        "city": "Bucarest",
        "founded": 1953,
        "arena": "Sala Polivalentă",
        "capacity": 5300,
        "colors": ["red", "white"],
        "successes_in_cl": {"1st": 1, "2nd": 1, "3rd": 0},
    },
    {
        "name": "RK Nexe Nasice",
        "country": "Croatia",
        "city": "Nasice",
        "founded": 1959,
        "arena": "Sportska",
        "capacity": 2500,
        "colors": ["green", "black"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    },
    {
        "name": "RK Croatia Zagreb",
        "country": "Croatia",
        "city": "Zagreb",
        "founded": 1922,
        "arena": "Arena Zagreb",
        "capacity": 15200,
        "colors": ["blue", "white", "red"],
        "successes_in_cl": {"1st": 2, "2nd": 4, "3rd": 0},
    },
    {
        "name": "Rhein Neckar Löwen",
        "country": "Germany",
        "city": "Lowen",
        "founded": 2002,
        "arena": "SAP Arena",
        "capacity": 14500,
        "colors": ["yellow", "navy blue"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 1},
    },
    {
        "name": "Valur",
        "country": "Iceland",
        "city": "Reykjavík",
        "founded": 1911,
        "arena": "N höllin",
        "capacity": 1300,
        "colors": ["red", "white"],
        "successes_in_cl": {"1st": 0, "2nd": 0, "3rd": 0},
    }
]


# 122, 123, 124
# _______________________________________________
# Write a function that return list of tuples and takes list of dictionaries
# question : What are the 3 oldest clubs (among those mentioned) and how many years ago were they founded ?

def three_oldest_club(data):
    sorted_clubs = sorted(data, key=lambda x: x['founded'])

    oldest_clubs = sorted_clubs[:3]

    current_year = 2024

    result = [(club['name'], current_year - club['founded']) for club in oldest_clubs]

    return result


assert three_oldest_club(handball_elite) == [('Fuechse Berlin', 133), ('THW Kiel', 120), ('Valur', 113)]


# 125, 126, 127
# _______________________________________________
# Write a function that return list of dictionary
# question : Has any club from Poland achieved success in the Champions League (successes_in_cl), if so, display information about it.

def check_polish_clubs(data):
    return [club for club in data if club['country'] == 'Poland' and
            (club['successes_in_cl']['1st'] > 0 or club['successes_in_cl']['2nd'] > 0 or
             club['successes_in_cl']['3rd'] > 0)]


assert check_polish_clubs(handball_elite) == [{'name': 'KS Iskra Kielce',
                                               'country': 'Poland',
                                               'city': 'Kielce',
                                               'founded': 1965,
                                               'arena': 'Hala Legionów',
                                               'capacity': 4200,
                                               'colors': ['yellow', 'blue', 'white'],
                                               'successes_in_cl': {'1st': 1, '2nd': 2, '3rd': 2}}]


# 128, 129, 130
# _______________________________________________
# Write a function that return list of tuples and takes list of dictionaries
# question : Which countries (name the top 3) are most represented by the clubs mentioned in the ranking?

def check_amount_country(data):
    country_counts = {}

    for club in data:
        country = club['country']
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1

    sorted_country_counts = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_country_counts[:3]


assert check_amount_country(handball_elite) == [('Germany', 5), ('France', 3), ('Denmark', 2)]

d = {
    "Poland": "Warsaw",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Canada": "Ottawa",
    "United States": "Washington, D.C.",
    "Japan": "Tokyo",
    "Australia": "Canberra"
}


# 131, 132, 133
# _______________________________________________
# Write a function that takes dictionary and return list  key/s that starts with J letter


def keys_start_with_j(any_dict):
    return [key for key, value in any_dict.items() if key.startswith('J')]


assert keys_start_with_j(d) == ['Japan']


# 134, 135, 136
# _______________________________________________
# Write a function that takes dictionary and return list of value/s that ends with n letter

def value_ends_with_n(any_dict):
    return [value for key, value in any_dict.items() if value.endswith('n')]


assert value_ends_with_n(d) == ['Berlin', 'London']


# 137, 138, 139
# _______________________________________________
# Write a function that takes dictionary and return list of
# keys when value/s starts with W and ends with w letter

def value_start_w_ends_w(any_dict):
    return [key for key, value in any_dict.items()
            if value.startswith('W') and value.endswith('w')]


assert value_start_w_ends_w(d) == ["Poland"]


# 139, 140, 141
# _______________________________________________
# Write a function that takes dictionary and return list of
# values when a letter or t letter exists 2 or more times

def value_key_value_count_a_t(any_dict):
    return [key for key, value in any_dict.items()
            if value.count('a') >= 2 or value.count('t') >= 2]


# print(value_key_value_count_a_t(d))
assert value_key_value_count_a_t(d) == ['Poland', 'Canada', 'Australia']


# 142, 143, 144
# for the list named handball_elite return list of countries that
# value of 'capacity' > 5000 nad value of 'country' <= 6

def give_l(list_dict):
    return [item['country'] for item in list_dict if item['capacity'] > 5000 and
            len(item['country']) <= 6]


assert give_l(handball_elite) == ['Spain', 'France', 'Poland', 'France']


# 145
# count method for str

def str_count(any_str):
    return any_str.count('a')


# print(str_count('Alice has a cat'))
assert str_count('Alice has a cat') == 3


# 146
# count method for str with lower

def str_count_lower(any_str):
    return any_str.lower().count('a')


assert str_count_lower('Alice has a cat') == 4

# 147
# find method for str

def str_find(any_str):
    return any_str.find('cat')

assert str_find('Alice has a cat') == 12

# 148, 149, 150
# for the list named handball_elite return list of cities that
# value of 'capacity' is not an odd number nad value of 'country' <= 6

def give_l_2(list_dict):
    return [item['city'] for item in list_dict if not item['capacity'] & 1 and
            len(item['country']) <= 6]

# print(give_l_2(handball_elite))
assert give_l_2(handball_elite) == ['Barcelona', 'Paris', 'Kielce', 'Montpellier', 'Płock', 'Nantes']

# 151
# index method for str

def str_index(any_str):
    return any_str.index('cat')

assert str_index('Alice has a cat') == 12

# 152
# index method for str ( parameters )

def str_index_par(any_str):
    return any_str.index('as',1 ,10)

assert str_index_par('Alice has a cat') == 7

# 153
# rfind method for str

def str_rfind(any_str):
    return any_str.find('cat')

assert str_rfind('Alice has a cat') == 12

data = [
    {
        "name": "pawel",
        "city": "krakow",
        "age": 39,
        "hobbies": ["js", "python", "drugs"]
    },
    {
        "name": "joanna",
        "city": "krakow",
        "age": 32,
        "hobbies": ["movies", "books", "food"]
    },
    {
        "name": "igor",
        "city": "wroclaw",
        "age": 31,
        "hobbies": ["anime", "games", "movies"]
    },
    {
        "name": "dawid",
        "city": "wroclaw",
        "age": 43,
        "hobbies": ["film", "music", "bike"]
    },
    {
        "name": "piotr",
        "city": "warszawa",
        "age": 35,
        "hobbies": ['wspinaczka', 'komputery', 'anime']
    },
    {
        "name": "tomek",
        "city": "warszawa",
        "age": 38,
        "hobbies": ["shooting", "sailing", "martial arts"]
    },
    {
        "name": "rafal",
        "city": "warszawa",
        "age": 28,
        "hobbies": ["cars", "IT"]
    },
    {
        "name": "mateusz",
        "city": "wroclaw",
        "age": 30,
        "hobbies": ["bjj", "python", "java"]
    },
    {
        "name": "adrian",
        "city": "dabrowa gornicza",
        "age": 33,
        "hobbies": ["reading", "video games", "chemistry", "physics", "boardgames", "shooting"]
    },
    {
        "name": "cezary",
        "city": "kielce",
        "age": 33,
        "hobbies": ["programming", "sport shooting", "paper models", "and more"],
    },
    {
        "name": "szymon",
        "city": "wroclaw",
        "age": 30,
        "hobbies": ["crypto", "podcasts", "games"]
    },
    {
        'name': 'piotr',
        'city': 'warszawa',
        'age': 50,
        'hobbies': ['python', 'snorkeling', 'traveling']
    },
    {
        "name": "igor",
        "city": "warszawa",
        "age": 34,
        "hobbies": ["golf", "music", "art"]
    },
    {
        "name": "marcin",
        "city": "krakow",
        "age": 40,
        "hobbies": ["python", "ds", "sleep"]
    },
    {
        "name": "kasia",
        "city": "krakow",
        "age": 35,
        "hobbies": ["music"]
    },
    {
        "name": "mateusz",
        "city": "dabrowa gornicza",
        "age": 31,
        "hobbies": ["filmy"]
    }
]


# 154
# write function that return average age of course users

def avg_age_01(data_):
    number_users = 0
    for user in data_:
        number_users += user['age']
    return number_users // len(data_)

assert avg_age_01(data) == 35

# 155, 156, 157
# the same task what # 154 but use the list comprehension

def avg_age_02(persons):
    age_sum = [person['age'] for person in persons]
    return sum(age_sum) // len(persons)

assert avg_age_02(data) == 35

# 158, 159, 160
# the same task what # 155 but use the generator expression
# with lambda and map functions

def avg_age_03(persons):
    return sum(list(map(lambda person: person['age'] , persons))) // len(persons)

assert avg_age_03(data) == 35

# 161, 162, 163
# create function that takes list of dictionaries and return
# dict with person and age for the people only from Warsaw , use dict comprehension

def people_from_warsaw(persons):
    return {person['name']: person['age'] for person in persons
            if 'warszawa'.lower() in person['city']}

assert people_from_warsaw(data) == {'piotr': 50, 'tomek': 38, 'rafal': 28, 'igor': 34}

# 164, 165, 166
# write function that return average age of course users only from warsaw

def avg_age_people_from_warsaw_(persons):
    r = {person['name']: person['age'] for person in persons
            if 'warszawa'.lower() in person['city']}
    return sum(r.values()) // len(r)

assert avg_age_people_from_warsaw_(data) == 37

# 167, 168, 169
# the same task what #164 but for the people from out of Warsaw
def avg_age_people_out_warsaw_(persons):
    r = {person['name']: person['age'] for person in persons
            if 'warszawa'.lower() not in person['city']}
    return sum(r.values()) // len(r)

# print(avg_age_people_from_warsaw_(data))
assert avg_age_people_out_warsaw_(data) == 34

# 171, 172, 173
# the same what #161 but for the people from out of Warsaw

def people_out_warsaw(persons):
    return {person['name']: person['age'] for person in persons
            if 'warszawa'.lower() not in person['city']}

# print(people_out_warsaw(data))

assert people_out_warsaw(data) == {'pawel': 39, 'joanna': 32, 'igor': 31, 'dawid': 43, 'mateusz': 31, 'adrian': 33, 'cezary': 33, 'szymon': 30, 'marcin': 40, 'kasia': 35}

# 174, 175, 176
# the same what # 171 but only list of names

def people_out_warsaw_names(persons):
    return [person['name'] for person in persons
            if 'warszawa'.lower() not in person['city']]

# print(people_out_warsaw_names(data))
assert people_out_warsaw_names(data) == ['pawel', 'joanna', 'igor', 'dawid', 'mateusz', 'adrian', 'cezary', 'szymon', 'marcin', 'kasia', 'mateusz']

# 177
# the same task what 167 but traditional method

def avg_age_people_out_warsaw_2(dataset):
    total_age = 0
    counter = 0

    for person in dataset:
        if person['city'].lower() != 'warszawa':
            total_age += person['age']
            counter += 1
    return total_age // counter

assert avg_age_people_out_warsaw_2(data) == 34

# 178, 179, 180
# using tuple comprehension create function that return
# people's names from warsaw

def give_back_names_people_from_waw(dataset):
    return tuple(names['name'] for names in dataset if names['city'].lower() == 'warszawa' )

# print(give_back_names_people_from_waw(data))
assert give_back_names_people_from_waw(data) == ('piotr', 'tomek', 'rafal', 'piotr', 'igor')

# 181
# the same what 180 but traditional method function has to return list

def give_back_names_people_from_waw_2(dataset):
    names = []
    for person in dataset:
        if person['city'].lower() == 'warszawa':
            names.append(person['name'])
    return names

# print(give_back_names_people_from_waw_2(data))
assert give_back_names_people_from_waw_2(data) == ['piotr', 'tomek', 'rafal', 'piotr', 'igor']

# 182, 183, 184
# the same what 181 but use lambda and map functions

def give_back_names_people_from_waw_3(people):
    return list(map(
        lambda person: person['name'],
        filter(lambda person: person['city'].lower() == 'warszawa', people)
    ))

# print(give_back_names_people_from_waw_3(data))
assert give_back_names_people_from_waw_3(data) == ['piotr', 'tomek', 'rafal', 'piotr', 'igor']

# 185, 186, 187
# create function that return set of cities without repetition
# use set comprehension

def cities_without_repetition(dataset):
    return set(city['city'] for city in dataset)

# print(cities_without_repetition(data))
assert cities_without_repetition(data) == {'krakow', 'dabrowa gornicza', 'wroclaw', 'kielce', 'warszawa'}

# 188
# the same task what # 185 but use traditional method and return list

def cities_without_repetition_2(dataset):
    cities = []
    for city in dataset:
        cities.append(city['city'])
    return list(set(cities))

print(cities_without_repetition_2(data))
# assert cities_without_repetition_2(data) == ['krakow', 'dabrowa gornicza', 'warszawa', 'kielce', 'wroclaw']

# 189, 190, 191
# the same what 185 bud use the lambda and map functions

def cities_without_repetition_3(dataset):
    return set(map(lambda city: city['city'], dataset))

assert cities_without_repetition_3(data) == {'wroclaw', 'krakow', 'warszawa', 'kielce', 'dabrowa gornicza'}

# 192, 193, 194
# write a function that check if someone is a geezer and return bool value True or False
# geezer is a person above 35

def check_age_people(dataset):
    return bool(len([age['name'] for age in dataset if age['age'] > 35]) > 1)

assert check_age_people(data) == True

# 195, 196, 197
# the same what # 192 but function has to return str with info about amount geezers in the group

def check_age_people_2(dataset):
    age_list = [age['name'] for age in dataset if age['age'] > 35]
    return f'There are {len(age_list)} people who are older than 35 years' if len(age_list) >= 1 else f'There is no elderly people in the group'

# print(check_age_people_2(data))
assert check_age_people_2(data) == 'There are 5 people who are older than 35 years'

# 198
# the same what # 192 but in traditional method

def check_age_people_3(dataset):
    age_list = []
    for age in dataset:
        if age['age'] > 35:
            age_list.append(age['name'])
    return True if len(age_list) > 1 else False

assert check_age_people_3(data) == True

# 199, 200, 201
# the same what # 192 but use map , lambda and filter

def check_age_people_4(dataset):
    ages = list(map
                (lambda person: person['name'],
                filter(lambda person_age: person_age['age'] > 35, dataset)
                ))
    return len(ages) > 1

assert check_age_people_4(data) == True

# 202, 203, 204
# write a function that takes str and capitalize every second letter for that string

def change_second_letter(any_str):
    return ''.join(
        char.upper() if index % 2 == 0 else char
        for index, char in enumerate(any_str)
    )

# print(change_second_letter('ala ma kota'))
assert change_second_letter('ala ma kota') == 'AlA Ma kOtA'

# 205, 206, 207
# write a function that takes list contains string and returns list of tuples

def create_tuple_from_list_of_string(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings)]

# print(create_tuple_from_list_of_string(['home', 'dog', 'funeral', 'dental']))
assert create_tuple_from_list_of_string(['home', 'dog', 'funeral', 'dental']) == [(0, 'home'), (1, 'dog'), (2, 'funeral'), (3, 'dental')]

# 208, 209, 210
# the same what # 205 but only for odd indexes

def create_tuple_from_list_of_string_odd(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings) if index & 1]

# print(create_tuple_from_list_of_string_odd(['home', 'dog', 'funeral', 'dental']))
assert create_tuple_from_list_of_string_odd(['home', 'dog', 'funeral', 'dental']) == [(1, 'dog'), (3, 'dental')]

# 211, 212, 213
# the same what # 205 but only for even indexes

def create_tuple_from_list_of_string_even(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings) if not index & 1]

# print(create_tuple_from_list_of_string_even(['home', 'dog', 'funeral', 'dental', 'word', 'war']))
assert create_tuple_from_list_of_string_even(['home', 'dog', 'funeral', 'dental', 'word', 'war']) == [(0, 'home'), (2, 'funeral'), (4, 'word')]

# 214, 215, 216
# the same what # 205 but every third index

def create_tuple_from_list_of_string_every_3th(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings) if index %3 == 0]

# print(create_tuple_from_list_of_string_every_3th(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert (create_tuple_from_list_of_string_every_3th(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9'])) == [(0, 'home'), (3, 'dental'), (6, '6'), (9, '9')]

# 217, 218, 219
# the same what # 214 all indexes except every third index

def create_tuple_from_list_of_string_except_every_3th(list_of_strings):
    return [(index, item) for index, item in enumerate(list_of_strings) if index %3 != 0]

# print(create_tuple_from_list_of_string_except_every_3th(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert (create_tuple_from_list_of_string_except_every_3th(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9'])) == [(1, 'dog'), (2, 'funeral'), (4, 'word'), (5, 'war'), (7, '7'), (8, '8')]

# 220, 221, 222
# write a function that takes list and return dictionary with odd keys

def create_dict_from_list_of_string_odd(list_of_strings):
    return {index: item for index, item in enumerate(list_of_strings) if index & 1}

# print(create_dict_from_list_of_string_odd(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert create_dict_from_list_of_string_odd(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']) == {1: 'dog', 3: 'dental', 5: 'war', 7: '7', 9: '9'}

# 223, 224, 225
# the same what # 220 but for even keys

def create_dict_from_list_of_string_even(list_of_strings):
    return {index: item for index, item in enumerate(list_of_strings) if not index & 1}

# print(create_dict_from_list_of_string_even(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert create_dict_from_list_of_string_even(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']) == {0: 'home', 2: 'funeral', 4: 'word', 6: '6', 8: '8'}

# 226, 227, 228
# the same what # 225 but for every 4th keys

def create_dict_from_list_every_4th_key(list_of_strings):
    return {index: item for index, item in enumerate(list_of_strings) if not index % 4 }

# print(create_dict_from_list_every_4th_key(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert create_dict_from_list_every_4th_key(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']) == {0: 'home', 4: 'word', 8: '8'}

# 229, 230, 231
# the same what # 226 but not for every 4th keys

def create_dict_from_list_not_every_4th_key(list_of_strings):
    return {index: item for index, item in enumerate(list_of_strings) if index % 4 != 0 }

# print(create_dict_from_list_not_every_4th_key(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']))
assert create_dict_from_list_not_every_4th_key(['home', 'dog', 'funeral', 'dental', 'word', 'war', '6', '7', '8', '9']) == {1: 'dog', 2: 'funeral', 3: 'dental', 5: 'war', 6: '6', 7: '7', 9: '9'}

# 232, 233, 234
# create function that change every second letter in the sentence

def every_second_letter(any_str):
    return ''.join(letter.lower() if index % 2 else letter.upper() for index, letter in enumerate(any_str))

# print(every_second_letter('home is roomy and i would like to buy it'))
assert every_second_letter('home is roomy and i would like to buy it') == 'HoMe iS RoOmY AnD I WoUlD LiKe tO BuY It'

# 235, 236, 237
# the same what 232 but opposite action , means start from small letter

def every_second_letter_first_small(any_str):
    return ''.join(letter.lower() if not index % 2 else letter.upper() for index, letter in enumerate(any_str))

# print(every_second_letter_first_small('home is roomy and i would like to buy it'))
assert every_second_letter_first_small('home is roomy and i would like to buy it') == 'hOmE Is rOoMy aNd i wOuLd lIkE To bUy iT'

# 238, 239, 240
# write function uses closure that outer function takes str and number
# inner function should apply title and after that swapcase method and multiply by number from outer function

def hello(name, a):
    def inner():
        return f'Hello {(" " + name.title().swapcase()) * a}'
    return inner

x_fn = hello('Love is in the air', 3)
# print(x_fn())

assert x_fn() == 'Hello  lOVE iS iN tHE aIR lOVE iS iN tHE aIR lOVE iS iN tHE aIR'

# 241, 242, 243
# create a decorator that change str by swapcase method in decorated function

def capitalize(fn):
    def inner(name):
        return fn(name.swapcase())
    return inner

@capitalize
def hello(name):
    return f'Hello {name}'

# print(hello('JoHn'))
assert hello('JoHn') == 'Hello jOhN'

# 244, 245, 246
# create a decorator that multiply result of decorated function by value

def multiply(fn):
    def inner(*args, c):
        return fn(*args) * c
    return inner

@multiply
def add(a, b):
    return a + b
result = add(1, 2, c=4)
# print(result)
assert result == 12







