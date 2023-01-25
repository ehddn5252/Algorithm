l1 = input()
l2 = input()
dp = [[0 for _ in range(len(l2))] for _ in range(len(l1))]

for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            dp[i][j] = 1

ans=0
for i in range(1, len(l1)):
    for j in range(1, len(l2)):
        if l1[i] == l2[j]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])
            if dp[i][j]>ans:
                ans = dp[i][j]

print(ans)