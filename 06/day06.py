#!/usr/bin/env python3

customs = [len(set(filter(None, i.replace('\n', '')))) for i in open('input.txt').read().split('\n\n')]
print(sum(customs))
