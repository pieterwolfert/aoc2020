#!/usr/bin/env python3

with open('input.txt') as f:
    rules = [i.strip() for i in f.readlines()]
bags = {}
for r in rules:
    rule = r.split(' bags contain')
    items = rule[1:][0].split(',')
    items = [i.replace(' bags', '').replace('.', '').replace(' bag', '') for i in items]
    items = [[i[1], i[3:]] for i in items]
    bags[rule[0]] = items

sg = []
visited = set()
for key in bags:
    items = bags[key]
    for i in items:
        if 'shiny gold' in i[1]:
            sg.append(key)

while len(sg) > 0:
    clr = sg.pop(0)
    if clr not in visited:
        for key in bags:
            items = bags[key]
            for i in items:
                if clr in i[1]:
                    sg.append(key)
    visited.add(clr)

