#!/usr/bin/env python3

passports = [filter(None, i.replace('\n', ' ').split(' ')) for i in open('input.txt', 'r').read().split('\n\n')]
passports = [dict(s.split(':') for s in p) for p in passports]
print(sum([all (k in p for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')) for p in passports]))
