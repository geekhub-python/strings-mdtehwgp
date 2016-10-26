#!/usr/bin/env python3

string = input('string: ')

first_entry = string.find('f')         # index 1-st entry if exist or '-1'
search_entry = string[first_entry+1:]  # search 2-nd entry
second_entry = search_entry.find('f')  # index 2-nd entry if exist or '-1'

if first_entry != -1 and second_entry != -1:
    print('index second entry', second_entry+len(string[:first_entry+1]))
elif first_entry == -1:
    print('-2')
else:
    print(second_entry)
