#!/usr/bin/env python3

with open('input.txt') as f:
    joltages = sorted([int(i.strip()) for i in f])
joltages.sort()
joltages = [0] + joltages + [max(joltages) + 3]


