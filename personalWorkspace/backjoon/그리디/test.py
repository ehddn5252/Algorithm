# 작성일자 : 20210202
# 문제명 : ATM
# 문제 풀이 : dp 점화식 dp[i]= dp[i-1]+dp[i] 를 만들면 각 사람이 기다리는 시간이 dp에 저장되는 데, 모든 사람이 기다린 총 시간이므로 
# sum(dp)를 하면 답이 된다.


import sys


def solution(numList):
    numList.sort()
    dp=numList[:]
    for i in range(1,len(numList)):
        dp[i]=dp[i-1]+dp[i]
    
    answer=sum(dp)
    print(answer)


if __name__=="__main__":
    _ = int(sys.stdin.readline())
    numList=list(map(int,sys.stdin.readline().split()))
    solution(numList)