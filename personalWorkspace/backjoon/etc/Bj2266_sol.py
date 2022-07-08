# Bj2266 금고 부수기 다시 생각해보기
N, K = map(int,input().split(" "))

INF = 9876543210

# dp 배열을 만들어 준다.
dp = [[0 for i in range(501)]for i in range(501)]

# dp 의 row 는 계란수, col 은 층 수이다.
# 초기 세팅
## 0 층은 0, 1 층은 한 개가 필요하다.
for i in range(1, K+1):
    dp[i][1] = 1
    dp[i][0] = 0
## 1개의 금고를 가지고는 N 번 해야한다.
for i in range(1, N+1):
    dp[1][i] = i

# 점화식 i와 j 가 2 이상부터
for i in range(2, K+1):
    for j in range(2, N+1):
        dp[i][j] = INF
        for k in range(1, j+1):
            # 현재 dp 값은 이전 층수들 중의 가장 큰 값 + 1 또는 금고 하나 적은 것들 중 최고 값 + 1이 된다.
            # dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k])), (k = 1 ~ j)  가 된다.
             tmp_value = 1 + max(dp[i-1][k-1], dp[i][j-k])
             dp[i][j] = min(dp[i][j], tmp_value)

print(dp[K][N])