n = int(input())

l = []
dp = []
for _ in range(n):
    l.append(int(input()) - 1)
    dp.append(1)

for i in range(n):
    for j in range(i, n):
        if l[i] < l[j]:
            dp[j] = max(dp[i] + 1, dp[j])

print(n-max(dp))