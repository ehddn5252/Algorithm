# 작성일자 20210201
# 문제명 : 백준 [2609] 최대공약수와 최소공배수
# 일단 GCF를 찾는다. i는 a부터 1까지를 a%i==0와b%i==0을 확인해본다
# a*b = GCF * LCM 이 성립한다.
# LCM = a*b//GCF

import sys
def findGCF(a,b):
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            return i

# a*b = GCF * LCM 이 성립한다.
# LCM = a*b//GCF
def solution(a,b):
    GCF=findGCF(a,b)
    print(GCF)
    LCM = a*b//GCF
    print(LCM)


if __name__=="__main__":
    a,b=map(int,sys.stdin.readline().split())
    if a>b:
        tmp=a
        a=b
        b=tmp
    solution(a,b)