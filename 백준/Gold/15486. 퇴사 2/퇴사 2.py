import sys

n = int(input())
l = []
dp = [0 for i in range(n + 1)]
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split(" "))))
for i in range(n):
    days = l[i][0]
    cost = l[i][1]
    for j in range(days):
        if i + j <= n:
            dp[i + j] = max(dp[i], dp[i + j])
        if i + days <= n:
            dp[i + days] = max(dp[i + days], dp[i + j], dp[i] + cost)
print(max(dp))
