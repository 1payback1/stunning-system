import math
from itertools import permutations
import random

#1
def grams_to_ounces(g):
    print(g * 28.3495231)

#2
def temp(F):
    print((5 / 9) * (F - 32))

#3
def solve(numheads, numlegs):
    print(numheads, " rabbits", numlegs / 2, " chickens")


def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

#4      
def filter_prime(list):
    for y in list:
        if is_prime(y):
            print(y)

#5
def perms(my_string):
    perms = permutations(my_string)
    for x in perms:
        print(''.join(x))

#6
def reverse_sentence(input_string):
    list_of_words = input_string.split()
    list_of_words.reverse()
    print(list_of_words)

#7
def has_33(my_list):
    for i in range(0, len(my_list) - 1):
        if my_list[i] == 3 and my_list[i + 1] == 3:
            return True
    return False

#8
def spy_game():
    print('Enter space-separated numbers: ')
    my_string = str(input())
    my_list_of_characters = my_string.split()
    my_list_of_integers = []
    for x in my_list_of_characters:
        my_list_of_integers.append(int(x))
    zero_count = 0
    flag = 0
    for x in my_list_of_integers:
        if x == 0:
            zero_count += 1
        elif x == 7 and zero_count >= 2:
            flag = 1
            break
    if flag == 1:
        print("True")
    else:
        print("False")

#9
def volume_of_sphere():
    print('Input radius: ')
    R = int(input())
    V = (4 / 3) * math.pi * (R ** 3)
    print(V)

#10
def unique_list(my_list):
    new_list = []
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
    print(new_list)

#11
def palindrome(my_string):
    for i in range(0, len(my_string)):
        if my_string[i] != my_string[len(my_string) - 1 - i]:
            return False
    return True

#12
def histogram(my_list):
    for x in my_list:
        s = ''
        for i in range(0, x):
            s = s + '*'
        print(s)

#13
def guess_the_number():
    print('Hello! What is your name?')
    name = str(input())
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    secret_number = random.randint(1, 20)
    attempts  = 0
    while True:
        print('Take a guess.')
        guess = int(input())
        attempts += 1
        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            print(f'Good job {name}! You guessed my number in {attempts} {'guess' if attempts == 1 else 'guesses'}!')
            break

