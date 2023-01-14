n, m = map(int, input().split(" "))

l = []
dp = [0 for _ in range(10001)]
v = []
for i in range(n):
    value = int(input())
    if value <= 10000:
        v.append(value)
v = list(set(v))
v.sort(reverse=True)
for i in range(len(v)):
    count = 1
    start = v[i]
    while start * count <= 10000:
        if dp[start * count] == 0:
            dp[start * count] = count
        else:
            dp[start * count] = min(count, dp[start * count])
        count += 1

for i in range(len(v)):
    for j in range(10001):
        if j - v[i] >= 0:
            if dp[j - v[i]] != 0:
                if dp[j]==0:
                    dp[j] = dp[j - v[i]] + 1
                else:
                    dp[j] = min(dp[j - v[i]] + 1,dp[j])
if dp[m]==0:
    print(-1)
else:
    print(dp[m])
