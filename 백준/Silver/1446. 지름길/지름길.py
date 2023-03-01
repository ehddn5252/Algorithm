N, D = map(int, input().split(" "))
dp = [i for i in range(D + 1)]
map1 = {}
shortcut = []
for _ in range(N):
    a, b, cost = map(int, input().split(" "))
    map1.setdefault((a, b), 10001)
    if b > D or b - a <= cost:
        continue
    if map1.get((a, b)) > cost:
        map1[(a, b)] = cost

for k, v in map1.items():
    shortcut.append([k[0], k[1], v])

for i in range(1, len(dp)):
    for j in shortcut:
        if j[1] == i and dp[j[0]] + j[2] < dp[i]:
            dp[i] = dp[j[0]] + j[2]
    dp[i] = min(dp[i - 1] + 1, dp[i])
l = [i for i in range(161)]
print(dp[D])
