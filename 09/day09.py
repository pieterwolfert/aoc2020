#!/usr/bin/env python3

with open('input.txt') as f:
    numbers = [int(i.strip()) for i in f]

invalid = 0

for i in range(25, len(numbers)-1):
    previous = [j for j in numbers[i-25:i]]
    summed = []
    for j in previous:
        for y in previous:
            if j != y:
                summed.append(j+y)
    if numbers[i] not in summed:
        invalid = numbers[i]

sliding_window = 2
found = False
while not found:
    for i in range(len(numbers) - (1 + sliding_window)):
        summed = sum(numbers[i:i+sliding_window])
        if summed == invalid:
            print(min(numbers[i:i+sliding_window]) + max(numbers[i:i+sliding_window]))
            found = True
    sliding_window += 1
        


