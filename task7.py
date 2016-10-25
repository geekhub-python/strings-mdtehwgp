#!/usr/bin/env python3

string = input('string: ')

l = string.find('h')
r = string.rfind('h')

new_string = string[l+1:r]
replaced_string = new_string.replace('h', 'H')
print(string[:l+1] + replaced_string + string[r:])
