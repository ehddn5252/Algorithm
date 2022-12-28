import sys

n = int(input())
dp = [0 for i in range(n + 1)]
for i in range(n):
    days,cost = map(int, sys.stdin.readline().split(" "))
    for j in range(days):
        if i + j <= n:
            dp[i + j] = max(dp[i], dp[i + j])
        if i + days <= n:
            dp[i + days] = max(dp[i + days], dp[i] + cost)
print(max(dp))
