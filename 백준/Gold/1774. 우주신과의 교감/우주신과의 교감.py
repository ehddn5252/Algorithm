def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]


def merge(u, v):
    global check
    check = False
    u = find(u)
    v = find(v)

    if u == v:
        return
    if u > v:
        parent[u] = v
    else:
        parent[v] = u
    check = True


def is_same_root(u, v):
    u = find(u)
    v = find(v)

    if u == v:
        return True
    else:
        return False


import sys

sys.setrecursionlimit(20000)
check = False
N, m = map(int, sys.stdin.readline().split(" "))
l = []
edge = []
parent = []
ans = 0
import math


def distance(a, b):
    return abs(math.sqrt((l[a][0] - l[b][0]) ** 2 + (l[a][1] - l[b][1]) ** 2))

for i in range(N):
    x, y = map(int, sys.stdin.readline().split(" "))
    l.append((x, y))
    parent.append(i)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    merge(a - 1, b - 1)

for i in range(len(l)):
    for j in range(i, len(l)):
        if i == j:
            continue
        edge.append((distance(i, j), i, j))

edge.sort()
for i in range(len(edge)):
    merge(edge[i][1],edge[i][2])
    if check:
        ans+=edge[i][0]
print("{:.2f}".format(ans))
