import json
import shutil

def full_width_equals():
    terminal_width, _ = shutil.get_terminal_size()
    return terminal_width

with open('sample-data.json') as file:
    data = json.load(file)

x0 = data['imdata'][0]['l1PhysIf']['attributes']['dn']
x1 = data['imdata'][1]['l1PhysIf']['attributes']['dn']
x2 = data['imdata'][2]['l1PhysIf']['attributes']['dn']

y0 = data['imdata'][0]['l1PhysIf']['attributes']['speed']
y1 = data['imdata'][1]['l1PhysIf']['attributes']['speed']
y2 = data['imdata'][2]['l1PhysIf']['attributes']['speed']

z0 = data['imdata'][0]['l1PhysIf']['attributes']['mtu']
z1 = data['imdata'][1]['l1PhysIf']['attributes']['mtu']
z2 = data['imdata'][2]['l1PhysIf']['attributes']['mtu']


print('Interface Status')
print('=' * full_width_equals())
print('DN' + 35 * ' ' + 'x.' + 11 * ' ' + 'Description' + 10 * ' ' + 'Speed' + 9 * ' ' + 'MTU')
print(42 * '-' + 5 * ' ' + 17 * '-' + 5 * ' ' + 9 * '-' + 5 * ' ' + 7 * '-')
print(x0 + 28 * ' ' + y0 + 8 * ' ' + z0)
print(x1 + 28 * ' ' + y1 + 8 * ' ' + z1)
print(x2 + 28 * ' ' + y2 + 8 * ' ' + z2)