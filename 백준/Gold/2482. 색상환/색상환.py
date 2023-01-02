N = int(input())
K = int(input())

dp = [[1 if j == 0 else i if j == 1 else 0 for j in range(N + 1)] for i in range(N + 1)]
for n in range(2, N + 1):
    for k in range(2, n):
        dp[n][k] = (dp[n - 2][k - 1] + dp[n - 1][k]) % 1000000003
print((dp[N - 3][K - 1] + dp[N - 1][K]) % 1000000003)
