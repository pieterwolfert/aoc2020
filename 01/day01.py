#!/usr/bin/env python

input_file = open('input.txt', 'r')
u = [int(i) for i in input_file.readlines()]
for one in u:
    for two in u:
        if one + two == 2020:
            print(one * two)
            quit(1)
