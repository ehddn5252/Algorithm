from pprint import pprint

N, M, K = map(int, input().split(" "))

orders = []
for i in range(N):
    # 치즈버거 수, 감튀 수
    orders.append(list(map(int, input().split(" "))))
dp = [[[0 for i in range(N)] for _ in range(M+1)] for _ in range(K+1)]

# 감자튀김 최대 수
for k in range(K+1):
    # 치즈버거 최대 수
    for j in range(M+1):
        for i in range(N):
            # 감튀수가 최대보다 작고, 치즈버거수가 최대보다 낮으면
            if k >= orders[i][1] and j >= orders[i][0]:
                dp[k][j][i] = max(dp[k-orders[i][1]][j-orders[i][0]][i-1]+1, dp[k][j][i-1],1)
            else:
                dp[k][j][i] = dp[k][j][i-1]
print(max(dp[K][M]))
