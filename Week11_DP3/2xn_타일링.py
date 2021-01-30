import sys


def solution(n):
    dp=[0]*1001
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[n]%10007)

if __name__=="__main__":
    n=int(sys.stdin.readline())
    solution(n)