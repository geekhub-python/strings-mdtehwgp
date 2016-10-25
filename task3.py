#!/usr/bin/env python3

s = input('string: ')
sep = len(s)//-2*(-1)
print(s[sep:] +  s[:sep])
