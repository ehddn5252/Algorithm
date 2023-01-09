N = int(input())
l = list(map(int, input().split(" ")))
INF = 999999
dp = [ INF for i in range(N)]

ans = 0
dp[0]=0
for i in range(0,N):
    for j in range(1,l[i]+1):
        if i+j<N:
            dp[i+j]=min(dp[i]+1,dp[i+j])

if dp[-1]!=INF:
    print(dp[-1])
else:
    print(-1)