def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]


def merge(u, v):
    u = find(u)
    v = find(v)

    if u == v:
        return
    if u > v:
        parent[u] = v
    else:
        parent[v] = u


def is_same_root(u, v):
    u = find(u)
    v = find(v)

    if u == v:
        return True
    else:
        return False


import sys
sys.setrecursionlimit(100000)
edge = []
check = False
V, m = map(int, sys.stdin.readline().split(" "))
l = []
parent = []
for i in range(V+1):
    parent.append(i)
for i in range(m):
    flag, a, b = map(int, sys.stdin.readline().split(" "))
    if flag == 0:
        merge(a, b)
    else:
        if is_same_root(a, b):
            print("YES")
        else:
            print("NO")
