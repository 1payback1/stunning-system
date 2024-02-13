import math

#1
def degrees_to_radians():
    angle_in_degrees = float(input('enter angle in degrees: '))
    radians = float(angle_in_degrees * (math.pi / 180))
    print(f'angle in radians {radians: 6f}')

#2
def area_of_trapezoid():
    height = int(input('enter height: '))
    first_base = int(input('enter first base: '))
    second_base = int(input('enter second base: '))
    area = 0.5 * (first_base + second_base) * height
    print(area)

#3
def area_of_regular_polygon():
    number_of_sides = int(input('enter number of sides: '))
    length_of_a_side = int(input('enter length of a side: '))
    area = int((number_of_sides * length_of_a_side ** 2) / (4 * math.tan(math.pi / number_of_sides)))
    print(area)

#4
def area_of_parallelogram():
    length_of_base = int(input('enter length of base: '))
    height = int(input('enter height: '))
    area = length_of_base * height
    print(area)

