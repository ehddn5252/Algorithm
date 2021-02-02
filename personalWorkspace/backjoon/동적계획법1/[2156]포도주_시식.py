# 작성일자 : 20210201
# 문제명 : 백준 2156 포도주 시식
# 문제 풀이: 
# 계단 오르기와 비슷한 문제이다. 다만 여기에서 dp점화식을 만들 때 더 주의해야 한다.
# dp[i]=max(dp[i-3]+wineList[i-1]+wineList[i],dp[i-2]+wineList[i],dp[i-1]) 에서 
# dp[i-3]+wineList[i-1]+wineList[i]는 현재꺼를 마시고 현재꺼 2번전 꺼를 안마시는 상태이다.(3번 연속 마시면 안됨)
# dp[i-2]+wineList[i]는 1번전 꺼를 안마시는 상태
# dp[i-1]은 현재꺼를 안마시는 상태이다.
# dp[i-1]를 생각하는 데 시간이 오래 걸렸다. 

import sys


def solution(wineList):
    dp=wineList[:]
    dp[1]=wineList[0]+wineList[1]
    dp[2]=max(dp[1],wineList[0]+wineList[2],wineList[1]+wineList[2])

    for i in range(3,len(wineList)):
        dp[i]=max(dp[i-3]+wineList[i-1]+wineList[i],dp[i-2]+wineList[i],dp[i-1])
    print(max(dp))




if __name__=="__main__":
    n= int(sys.stdin.readline())
    #n=6
    wineList=[]
    #wineList=[6, 10, 13, 9, 8, 1]
    
    for i in range(n):
        wineList.append(int(sys.stdin.readline()))
    
    if n==1:
        print(wineList[0])
    elif n==2:
        print(wineList[0]+wineList[1])
    else:
        solution(wineList)

