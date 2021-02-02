# 작성일자 : 20201231
# 작성자 : 김동우
# 문제명 : 다이얼 (백준 5622)

import sys

def findI(i):
    retValue=0
    if i =="A" or i=="B" or i=="C":
        retValue=3
    elif i=="D" or i=="E" or i=="F":
        retValue=4
    elif i=="G" or i=="H" or i=="I":
        retValue=5
    elif i=="J" or i=="K" or i=="L":
        retValue=6
    elif i=="M" or i=="N" or i=="O":
        retValue=7
    elif i=="P" or i=="Q" or i=="R" or i=="S":
        retValue=8
    elif i=="T" or i=="U" or i=="V":
        retValue=9
    elif i=="W" or i=="X" or i=="Y" or i=="Z":
        retValue=10
    return retValue

def solve():
    n= sys.stdin.readline()
    
    sumValue=0
    for i in n:
        sumValue+=findI(i)
    print(sumValue)
if __name__ == "__main__":
    solve()