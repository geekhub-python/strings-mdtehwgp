#!/usr/bin/env python3

string = input('string(len > 5): ')

string_out = (string[2], string[-2], string[:5],
              string[:-2], len(string), string[::2],
              string[1::2], string[::-1], string[::-2])

for string in string_out:
    print(string)
