from itertools import combinations_with_replacement

n, m = map(int, input().split(" "))
l = [i for i in range(1, n + 1)]
for i in combinations_with_replacement(l, m):
    print(" ".join(str(j) for j in i))
