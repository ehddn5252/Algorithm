# 작성일자 20210202
# 문제명 : 백준 [11866] 요세푸스 문제 0
# 문제 요약 : 
# 문제 풀이 최대 1000이니 2중 for문이 가능하다


import sys


def solution(N,K):
    yosepooseList=[i for i in range(1,N+1)]
    ansString="<"

    popNum = 0
    while len(yosepooseList) >0:
        popNum = (popNum + (K-1)) % len(yosepooseList)
        popElemnet = yosepooseList.pop(popNum)
        if len(yosepooseList)==0:
            ansString+=(str(popElemnet)+">")
        else:
            ansString+=(str(popElemnet)+", ")
    print(ansString)
if __name__=="__main__":
    N,K=map(int,sys.stdin.readline().split())
    solution(N,K)