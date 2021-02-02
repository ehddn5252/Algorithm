# 작성일자 : 20201231
# 작성자 : 김동우
# 문제명 : 크로아티아 알파벳 (백준 2941)
# c= c- dz= d- lj nj s= z=

import sys


def solve():
    inputedStr= sys.stdin.readline()
    ans=len(inputedStr)-1
    for index,value in enumerate(inputedStr):
        if value=='c':
            if inputedStr[index+1]=='-' or inputedStr[index+1]=='=':
                ans-=1
        if value=='d':
            if inputedStr[index+1]=='z':
                if inputedStr[index+2]=='=':
                    ans-=2
                    
            if inputedStr[index+1]=='-':
                ans-=1
        if value=='l':
            if inputedStr[index+1]=='j':
                ans-=1
        if value=='n':
            if inputedStr[index+1]=='j':
                ans-=1
        if value=='s':
            if inputedStr[index+1]=='=':
                ans-=1
        if value=='z':
            if inputedStr[index+1]=='=':
                if inputedStr[index-1]=='d':
                    continue
                else:
                    ans-=1
    print(ans)

if __name__ == "__main__":
    solve()