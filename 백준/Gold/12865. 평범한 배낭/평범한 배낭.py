N, K = map(int, input().split(" "))
# W,V
dp = [[0 for _ in range(100001)] for _ in range(101)]
w = [0 for _ in range(101)]
v = [0 for _ in range(101)]
for i in range(N):
    W, V = map(int, input().split(" "))
    w[i] = W
    v[i] = V
for i in range(N+1):
    for j in range(K+1):
        if j-w[i]>=0:
            dp[i][j] = max(dp[i-1][j-w[i]]+v[i],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(max(max(dp)))