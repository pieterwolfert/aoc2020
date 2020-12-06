#!/usr/bin/env python3

customs = [list(filter(None, i.replace('\n', ' ').split(' ' ))) for i in open('input.txt').read().split('\n\n')]

list_lengths = []
for c in customs:
    if len(c) > 0:
        sets = [set(i) for i in c]
        sets = sets[0].intersection(*sets)
        list_lengths.append(len(sets))
print(sum(list_lengths))
