#!/usr/bin/env python3

string = input('string: ')

l = string.find('h')
r = string.rfind('h')

s = string[l+1:r]

print(s[::-1])
