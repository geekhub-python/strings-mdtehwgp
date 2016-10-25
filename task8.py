#!/usr/bin/env python3

string = input('string: ')

l = string.find('f')
r = string.rfind('f')

if l and r == -1:
    pass
elif l == r:
    print('index: ', l)
else:
    print('first index: {} || last index: {}'.format(l, r))
