import re

with open('/Users/alibekzholdasbekov/Desktop/pp2/labs/lab5/row.txt', 'r') as file:
    data = file.readlines()


#1
def f1():
    pattern1 = r'ab*'
    flag = 0
    for line in data:
        match = re.search(pattern1, line)
        if match:
            flag = 1
            break
    if flag == 1:
        print(match.group())
    else:
        print(0)

#2
def f2():
    pattern2 = r'abb|abbb'
    flag = 0
    for line in data:
        match = re.search(pattern2, line)
        if match:
            flag = 1
            break
    if flag == 1:
        print(match.group())
    else:
        print(0)

#3
def f3():
    pattern3 = r'\b[a-z_]+_[a-z]+\b'
    matches = []
    for line in data:
        matches += re.findall(pattern3, line)
    print(matches)

#4
def f4():
    pattern4 = r'\b[A-Z][a-z]*\b'
    matches = []
    for line in data:
        matches += re.findall(pattern4, line)
    print(matches)

#5
def f5():
    pattern5 = r'a.*b$'
    flag = 0
    for line in data:
        match = re.search(pattern5, line)
        if match:
            flag = 1
            break
    if flag == 1:
        print(match.group())
    else:
        print(0)

#6
def f6():
    pattern6 = r'[ ,.]'
    for line in data:
        result = re.sub(pattern6, ':', line)
        print(result)

#7
def f7():
    pattern7 = r'_([a-z])'
    for line in data:
        result = ' '.join(re.sub(pattern7, lambda match : match.group(1).upper(), word) for word in line.split())
        print(result)

#8
def f8():
    pattern8 = r'[A-Z]'
    for line in data:
        parts = re.split(pattern8, line)
        result = ' '.join(parts)
        print(result)

#9
def f9():
    pattern9 = r'([a-z])([A-Z])'
    for line in data:
        result = re.sub(pattern9, r'\1 \2', line)
        print(result)

#10
def f10():
    pattern10 = r'([a-z0-9])([A-Z])'
    for line in data:
        result = re.sub(pattern10, r'\1_\2', line).lower()
        print(result)
