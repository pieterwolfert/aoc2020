#!/usr/bin/env python
import re

input_file = open('input.txt', 'r')
passwords = input_file.readlines()

valid = 0

for p in passwords:
    split_p = p.split(' ')
    bounds = re.split('-', split_p[0])
    lower_bound = int(bounds[0])
    upper_bound = int(bounds[1])
    character = split_p[1][:-1]
    password_string = split_p[2][:-1]
    if re.match(character + '*', password_string):
        count = password_string.count(character)
        if count >= lower_bound and count <= upper_bound:
            valid += 1
print(valid)



