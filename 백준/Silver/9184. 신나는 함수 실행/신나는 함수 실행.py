dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        dp[i][j][0] = 1
        dp[i][0][j] = 1
        dp[0][i][j] = 1
"""
a<=0 or b<=- or c<=-: 1
a>20, b> 20 c >20:
w(20)
if a<b<c:
dp[a][b][c] = dp[a][b][c-1] +dp[a][b-1][c-1] -dp[a][b-1][c]
else:
dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]
"""

for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
            else:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]
while True:
    a, b, c = map(int, input().split(" "))
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = ", end="")
    if a <= 0 or b <= 0 or c <= 0:
        value = 1
    elif a > 20 or b > 20 or c > 20:
        value = dp[20][20][20]
    else:
        value = dp[a][b][c]
    print(value)
