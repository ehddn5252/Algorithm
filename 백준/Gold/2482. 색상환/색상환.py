dp = [[0 for i in range(1001)] for _ in range(1001)]

N = int(input())
K = int(input())

for i in range(1001):
    dp[i][0] = 1
    dp[i][1] = i

for n in range(2, 1001):
    for k in range(2, n):
        dp[n][k] = (dp[n - 2][k - 1] + dp[n - 1][k]) % 1000000003

print((dp[N - 3][K - 1] + dp[N - 1][K]) % 1000000003)
