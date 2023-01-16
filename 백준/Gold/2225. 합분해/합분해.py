N, K = map(int, input().split(" "))

dp = [[0 for i in range(N + 1)] for _ in range(K + 1)]
for j in range(len(dp[0])):
    dp[1][j] = 1

for i in range(1, K + 1):
    for j in range(N + 1):
        for l in range(j + 1):
            dp[i][j] = (dp[i][j] + dp[i - 1][j - l]) % 1000000000

print(dp[K][N])
