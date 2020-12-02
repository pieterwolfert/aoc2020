#!/usr/bin/env python
import re

input_file = open('input.txt', 'r')
passwords = input_file.readlines()

valid = 0

for p in passwords:
    split_p = p.split(' ')
    bounds = re.split('-', split_p[0])
    pos_one = int(bounds[0]) - 1 
    pos_two = int(bounds[1]) - 1
    character = split_p[1][:-1]
    password_string = split_p[2][:-1]
    a = bool(password_string[pos_one] == character)
    b = bool(password_string[pos_two] == character)
    if (a and not b) or (not a and b):
        valid += 1
print(valid)
    
