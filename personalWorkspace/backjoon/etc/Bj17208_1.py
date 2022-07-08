from pprint import pprint

N, M, K = map(int, input().split(" "))

orders = []
for i in range(N):
    # 치즈버거 수, 감튀 수
    orders.append(list(map(int, input().split(" "))))

dp = [[[0 for i in range(K+1)] for _ in range(M+1)] for _ in range(N)]

for i in range(N):
    for j in range(M+1):
        for k in range(K+1):
            if k >= orders[i][1] and j >= orders[i][0]:
                dp[i][j][k] = max(dp[i-1][j-orders[i][0]][k-orders[i][1]]+1, dp[i-1][j][k])
            else:
                dp[i][j][k] = dp[i-1][j][k]
print(dp[N-1][M][K])
