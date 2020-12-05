#!/usr/bin/env python3


def getSeat(seatnumber):
    rowlower = 0
    rowupper = 127
    columnlow = 0
    columnhigh = 7
    for s in seatnumber:
        if s is 'F':
            rowupper -= (rowupper-rowlower+1)/2
        if s is 'B':
            rowlower += (rowupper-rowlower+1)/2
        if s is 'R':
            columnlow += (columnhigh-columnlow+1)/2
        if s is 'L':
            columnhigh -= (columnhigh-columnlow+1)/2
    return (rowlower*8) + columnlow


if __name__=="__main__":
    seats = open('input.txt').read().split()
    seatID = []
    for seatnumber in seats:
        seatID.append(getSeat(seatnumber))
    print(max(seatID))
    seatID.sort()
    for s in seatID:
        if s-1 not in seatID and s != seatID[0]:
            print(s-1)

