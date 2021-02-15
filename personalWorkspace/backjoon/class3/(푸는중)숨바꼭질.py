

# 숨바꼭질 푸는중 https://www.acmicpc.net/problem/1697
from sys import stdin

if __name__=="__main__":
    subinLocation,brotherLocation=map(int,stdin.readline().split())
    dp=[0]*100001
    for i in range(subinLocation-1,-1,-1):
        dp[i]+=1+dp[i+1]

    for i in range(subinLocation,len(dp)-1):
        if (i+1)%2==0:
            dp[i+1]=min(dp[i],dp[(i+1)//2])+1
        else:# 이 부분이 문제
            dp[i+1]=dp[i]+1
    print(dp[brotherLocation])

