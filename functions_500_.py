# This is a set of 500 pieces python functions

from math import pi

#001
#_______________________________________________
# adding two numbers

def add_num(a, b):
    return a + b

assert add_num(2,5) == 7

#002
#_______________________________________________
# subtracting two numbers

def subtract_num(a, b):
    return a - b

assert subtract_num(2,5) == -3

#003
#_______________________________________________
# multiplying two numbers

def multiply_num(a, b):
    return a * b

assert multiply_num(2,5) == 10

#004
#_______________________________________________
# dividing two numbers

def divide_num(a, b):
    return a / b

assert divide_num(2,5) == 0.4

#005
#_______________________________________________
# subtracting two numbers without the rest

def divide_num_without_rest(a, b):
    return a // b

assert divide_num_without_rest(2,5) == 0

#006
#_______________________________________________
# exponentiation of two numbers

def exponentiation_num(a, b):
    return a ** b

assert exponentiation_num(5,2) == 25

#007
#_______________________________________________
# square root

def count_square_root(a):
    return a ** 0.5

assert count_square_root(4) == 2

#008
#_______________________________________________
# BMI calculator

def bmi(mass, height):
    return mass / height ** 2

assert bmi(89, 1.8) == 27.469135802469133

#009
#_______________________________________________
# check word is palindrome

def check_palindrome(word):
    return word == word[::-1]

assert check_palindrome("hello") == False

#010
#_______________________________________________
# count square area

def square_area(a):
    return a*a

assert square_area(4) == 16

#011
#_______________________________________________
# count rectangle area

def rectangle_area(a, b):
    return a * b

assert rectangle_area(2,3) == 6

#012
#_______________________________________________
# count triangle area

def triangle_area(a, b, h):
    return 0.5 * (a + b) * h

assert triangle_area(2,3,4) == 10

#013
#_______________________________________________
# count perimeter of a square

def square_perimeter(a):
    return a * 4

assert square_perimeter(4) == 16

#014
#_______________________________________________
# count perimeter of a rectangle

def perimeter_rectangle(a, b):
    return 2 * (a + b)

assert perimeter_rectangle(4, 4) == 16

#015
#_______________________________________________
# count perimeter of a triangle

def perimeter_triangle(a, b, c):
    return a + b + c

#016
#_______________________________________________
# count circumference of a circle

def circumference_circle(r):
    return 2 * pi * r

assert circumference_circle(4) == 25.132741228718345

#017
#_______________________________________________
# count circle area

def circle_area(r):
    return pi * r * r

assert circle_area(2) == 12.566370614359172

#018
#_______________________________________________
# count trapezoid area

def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

assert trapezoid_area(4, 4, 4) == 16

#019
#_______________________________________________
# count trapezoid perimeter

def trapezoid_perimeter(a, b, c, d):
    return a + b + c + d

assert trapezoid_perimeter(4, 4, 4, 4) == 16

#020
#_______________________________________________
# count cube volume

def cube_volume(a):
    return a ** 3

assert cube_volume(4) == 64

#021
#_______________________________________________
# count cube total surface area

def cube_total_surface_area(a):
    return 6 * a * a

assert cube_total_surface_area(2) == 24

#022
#_______________________________________________
# count cuboid volume

def cuboid_volume(a, b, c):
    return a * b * c

assert cuboid_volume(4, 4, 4) == 64

#023
#_______________________________________________
# count cuboid total surface area

def cuboid_total_surface_area(a, b, c):
    return 2 * (a * b + a * c + b * c)

assert cuboid_total_surface_area(4, 4, 4) == 96

#024
#_______________________________________________
# count sphere area

def sphere_area(r):
    return 4/3 * pi * r ** 3

assert sphere_area(4) == 268.082573106329

#025
#_______________________________________________
# count sphere volume

def sphere_volume(r):
    return 4 * pi * r ** 2

assert sphere_volume(4) == 201.06192982974676

#026
#_______________________________________________
# count cone volume

def cone_volume(r, h):
    return 1/3 * pi * r ** 2 * h

assert cone_volume(4, 4) == 67.02064327658225

#027
#_______________________________________________
# count cone total area

def cone_total_surface_area(r, l):
    return pi * r * (r + l)

assert cone_total_surface_area(4, 4) == 100.53096491487338

#028
#_______________________________________________
# count cylinder total area

def cylinder_area(r, h):
    return 2 * pi * r * ( r + h) == 201.06192982974676

#029
#_______________________________________________
# count cylinder volume

def cylinder_volume(r, h):
    return pi * r ** 2 * h

assert cylinder_volume(4, 5) == cylinder_volume(4, 5)

#030
#_______________________________________________
# count pyramid volume square based

def pyramid_volume_square_based(a, h):
    return 1/3 * a ** a * h

assert pyramid_volume_square_based(4, 4) == 341.3333333333333


















