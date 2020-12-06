#!/usr/bin/env python3

customs = [list(filter(None, i.replace('\n', ' ').split(' ' ))) for i in open('input.txt').read().split('\n\n')]
customs = [[set(i) for i in c] for c in customs]
customs = [len(sets[0].intersection(*sets)) for sets in customs if len(sets) > 0]
print(sum(customs))
