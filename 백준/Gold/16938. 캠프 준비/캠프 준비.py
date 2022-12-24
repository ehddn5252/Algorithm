from itertools import combinations

N, L, R, X = map(int, input().split(" "))
l = list(map(int, input().split(" ")))
ans = 0
for k in range(2, N+1):
    for i in combinations(l, k):
        sum_value = sum(list(i))
        min_value = min(i)
        max_value = max(i)
        if sum_value >= L and sum_value <= R and max_value - min_value >= X:
            ans += 1

print(ans)