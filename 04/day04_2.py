#!/usr/bin/env python3
import re

passports = [filter(None, i.replace('\n', ' ').split(' ')) for i in open('input.txt', 'r').read().split('\n\n')]
passports = [dict(s.split(':') for s in p) for p in passports]
passports = [p for p in passports if all (k in p for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))]
print(sum([sum(
    [int(p['byr'].isdigit() and int(p['byr']) in range(1920, 2003))
    ,int(p['iyr'].isdigit() and int(p['iyr']) in range(2010, 2021))
    ,int(p['eyr'].isdigit() and int(p['eyr']) in range(2020, 2031))
    ,int('cm' in p['hgt'] and int(p['hgt'][:-2]) in range(150, 194))
    ,int('in' in p['hgt'] and int(p['hgt'][:-2]) in range(59, 77))
    ,int(0 if re.match("^#[0-9a-f]{6}", p['hcl']) is None else 1)
    ,int(p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    ,int(p['pid'].isdigit() and len(p['pid']) == 9)]) == 7 for p in passports]))



    
