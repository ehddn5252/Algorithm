# 피보나치 수

dp = [0] * 10001
dp[1] = 1
for i in range(2, 10001):
    dp[i] = dp[i - 1] + dp[i - 2]

num = int(input())
print(dp[num])
