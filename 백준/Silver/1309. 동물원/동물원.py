n = int(input())

dp = [0 for i in range(n+1)]
dp[0]=1
dp[1]=3
for i in range(2,n+1):
    dp[i]=(dp[i-1]*2 + dp[i-2])%9901

print(dp[n]%9901)