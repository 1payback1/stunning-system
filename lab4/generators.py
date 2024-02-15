#1
def square_numbers(N):
    x = 0
    while x < N:
        yield x ** 2
        x += 1

#2
def even_numbers(n):
    x = 0
    while x < n + 1:
        yield x
        x += 2
my_list = []
for x in even_numbers(int(input('Enter the number: '))):
    my_list.append(x)
print(my_list)

#3
def divisible_by_3_and_4(n):
    x = 0
    while x < n + 1:
        if x % 3 == 0 and x % 4 == 0:
            yield x
        x += 1

#4
def squares(a, b):
    while a < b + 1:
        yield a ** 2
        a += 1
for x in squares(2, 4):
    print(x)

#5
def numbers_from_n_down_to_0(n):
    while n >= 0:
        yield n
        n -= 1
