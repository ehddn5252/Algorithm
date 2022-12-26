from itertools import product

n, m = map(int, input().split(" "))
l = [i for i in range(1, n + 1)]
for i in product(l, repeat=m):
    print(" ".join(str(j) for j in i))
