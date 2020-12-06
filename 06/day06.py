#!/usr/bin/env python3

print(sum([len(set(filter(None, i.replace('\n', '')))) for i in open('input.txt').read().split('\n\n')]))
