N = int(input())
l = []
dp = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    l.append(list(map(int, input().split(" "))))
dp[0][0]=1
for i in range(N):
    for j in range(N):
        for k in range(1, N):
            if j - k >= 0 and l[i][j - k] == k:
                dp[i][j] = dp[i][j] + dp[i][j - k]

            if i - k >= 0 and l[i - k][j] == k:
                dp[i][j] = dp[i][j] + dp[i - k][j]
print(dp[N - 1][N - 1])
