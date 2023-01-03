n = int(input())
l = list(map(int, input().split(" ")))

INF = 9999999999
max_value = -INF


def dfs(l1, now, v):
    global max_value
    if now == n - 1:
        max_value = max(v, max_value)

    for i in range(1, len(l1) - 1):
        new_l = l1[:i] + l1[i + 1:]
        dfs(new_l, now + 1, v + l1[i - 1] * l1[i + 1])


for i in range(1, n - 1):
    dfs(l, i, 0)

print(max_value)
