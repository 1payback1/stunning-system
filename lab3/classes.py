import math

#1
class My_class():
    def __init__(self):
        self.my_string = ''
    def get_string(self):
        self.my_string = str(input('Enter a string: '))
    def print_string(self):
        print(self.my_string.upper())

#2
class Shape():
    def __init__(self):
        pass
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length * self.length)

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)

#4
class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, ' ', self.y)
    def move(self, new_x = 0, new_y = 0):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point_x = 0, other_point_y = 0):
        print(math.sqrt((other_point_x - self.x)**2 + (other_point_y - self.y)**2))

#5
class Bank_account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposit of {amount} successful. New balance: {self.balance}')
        else:
            print(f'Invalid deposit amount. Please enter a positive value.')
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawal of {amount} successful. New balance: {self.balance}')
        else:
            print('Invalid withdrawal amount.')

#6
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
list_of_numbers = [1, 2, 3, 4, 5, 6, 7]
list_of_primes = list(filter(lambda x : is_prime(x), list_of_numbers))