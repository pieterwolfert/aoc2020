#!/usr/bin/env python3

with open('input.txt') as f:
    numbers = [int(i.strip()) for i in f]

invalid = 0
for i in range(25, len(numbers)-1):
    if numbers[i] not in [j + y for j in numbers[i-25:i] for y in numbers[i-25:i] if j != y]:
        invalid = numbers[i]
        break

sliding_window = 2
found = False
while not found:
    for i in range(len(numbers) - (1 + sliding_window)):
        if invalid == sum(numbers[i:i+sliding_window]):
            print(min(numbers[i:i+sliding_window]) + max(numbers[i:i+sliding_window]))
            found = True
    sliding_window += 1
