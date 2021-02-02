# 작성일자 : 20210201
# 문제 명 : 백준 [1259] 팰린드롬수
# 문제 풀이 : 거꾸로 읽어도 똑같은 수가 팰린드롬 수이다 예를들어 131 12421 515 등
# 수가 주어질 때 팰린드롬 수 인지 확인하시오

import sys

def solution(n):
    strN=str(n)
    reversedStrN=strN[::-1]
    for i in range(len(strN)):
        if strN[i]!=reversedStrN[i]:
            print("no")
            return
    print("yes")

            

if __name__=="__main__":
    while True:
        n=int(sys.stdin.readline())
        if n==0: 
            break
        solution(n)
