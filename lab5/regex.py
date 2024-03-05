import re

with open('row.txt', 'r', encoding = 'utf-8') as file:
    data = file.readline()

#1
pattern1 = r'ab*'
x1 = re.search(pattern1, data)

#2
pattern2 = r'abb|abbb'
for line in data:
    x2 = re.search(pattern2, line)
    if x2:
        break
        print(1)
if x2 == False:
    print(0)

#3
pattern3 = r'\b[a-z]+_[a-z]+\b'
x3 = re.findall(pattern3, data)

#4
pattern4 = r'\b[A-Z][a-z]*\b'
x4 = re.findall(pattern4, data)

#5
pattern5 = r'\ba.*b\b'
x5 = re.search(pattern5, data)

#6
pattern6 = r'[ ,.]'
x6 = re.sub(pattern6, ':', data)

#7
pattern7 = r'([a-z])_([a-z])'
x7 = re.sub(pattern7, lambda a : a.group(1) +  a.group(2).upper(), data)

#8
pattern8 = r'[A-Z]'
x8 = re.split(pattern8, data)

#9
pattern9 = r'([a-z])([A-Z])'
x9 = re.sub(pattern9, lambda a : a.group(1) + ' ' + a.group(2), data)

#10
pattern10 = r'([a-z])([A-Z])'
x10 = re.sub(pattern10, lambda a : a.group(1) + '_' + a.group(2).lower(), data)