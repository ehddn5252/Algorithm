# 작성일자 : 20201231
# 작성자 : 김동우
# 문제명 : 상수 백준 2908

import sys

def solve():
    n= sys.stdin.readline()
    num1=""
    num2=""
    num1+=n[2]
    num1+=n[1]
    num1+=n[0]
    num2+=n[6]
    num2+=n[5]
    num2+=n[4]
    if int(num2)>int(num1):
        print(num2)
    else:
        print(num1)

if __name__ == "__main__":
    solve()