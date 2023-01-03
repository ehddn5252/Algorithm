from itertools import combinations

N = int(input())
INF = 11000000001
min_value = INF
max_value = -INF
l = list(map(int, input().split(" ")))
plus, minus, multi, divide = map(int, input().split(" "))


def dfs(plus, minus, multi, divide, sum_value, now):
    global max_value, min_value
    if now == N - 1:
        max_value = max(max_value, sum_value)
        min_value = min(min_value, sum_value)
        return
    if plus != 0:
        dfs(plus - 1, minus, multi, divide, sum_value + l[now + 1], now + 1)
    if minus != 0:
        dfs(plus, minus - 1, multi, divide, sum_value - l[now + 1], now + 1)
    if multi != 0:
        dfs(plus, minus, multi - 1, divide, sum_value * l[now + 1], now + 1)
    if divide != 0:
        if sum_value < 0:
            sum_value = (-sum_value) // l[now + 1] * -1
        else:
            sum_value = sum_value // l[now + 1]
        dfs(plus, minus, multi, divide - 1, sum_value, now + 1)


dfs(plus, minus, multi, divide, l[0], 0)
print(max_value)
print(min_value)
