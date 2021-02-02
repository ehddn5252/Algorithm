# 작성일자 20210202
# 문제명 : 백준 [11050] 이항계수
# 문제 요약 : 


import sys


def solution(N,K):
    Numerator=1
    denominator=1
    for i in range(N,N-K,-1):
        Numerator*=i
    for i in range(1,K+1):
        denominator*=i
    print(Numerator//denominator)


if __name__=="__main__":
    N,K=map(int,sys.stdin.readline().split())
    solution(N,K)
