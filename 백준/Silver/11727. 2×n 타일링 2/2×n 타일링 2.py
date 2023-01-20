n = int(input())
dp = [ 1 for _ in range(1001)]

for i in range(2,n+1):
    dp[i]=(dp[i-2]*2 + dp[i-1])%10007
print(dp[n])