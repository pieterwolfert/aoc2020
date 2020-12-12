#!/usr/bin/env python3

with open('input.txt') as f:
    joltages = sorted([int(i.strip()) for i in f])
joltages.sort()
jolts = [1, 1]

for j in range(len(joltages)-1):
    if joltages[j+1] - joltages[j] == 1:
        jolts[0] += 1
    elif joltages[j+1] - joltages[j] == 3:
        jolts[1] += 1

print(jolts[0]*jolts[1])

