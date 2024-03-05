import functools
import operator
import time
import math

#1
def multiply_list(list):
    result = functools.reduce(operator.mul, list, 1)
    return result

#2
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

#3
def is_palindrome(string):
    modified_string = ''.join(string.split())
    return modified_string == modified_string[::-1]

#4
def square_root(number, milliseconds):
    time.sleep(milliseconds / 1000.0)
    result = math.sqrt(number)
    if milliseconds > 1.0:
        print(f'Square root of {number} after {milliseconds} milliseconds is {result}')
    else:
        print(f'Square root of {number} after {milliseconds} millisecond is {result}')