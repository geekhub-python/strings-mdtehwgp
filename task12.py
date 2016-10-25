#!/usr/bin/env python3

string = input('string: ')
new_str = ''

for i, k in enumerate(string):
    if i == 0:
        new_str += k
    elif i % 3 != 0:
        new_str += k
    else:
        pass

print(new_str)
