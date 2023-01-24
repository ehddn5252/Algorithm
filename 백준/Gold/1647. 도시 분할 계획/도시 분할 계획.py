import sys


def find(a):
    global parent
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def merge(a, b):
    global check
    check = False
    a = find(a)
    b = find(b)
    if a == b:
        return

    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    check = True


N, M = map(int, input().split(" "))
edges = []
parent = [i for i in range(N)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    edges.append((c, a - 1, b - 1))

edges.sort()
ans = 0
max_value=-1
for i in range(len(edges)):
    merge(edges[i][1], edges[i][2])
    if check:
        max_value=max(max_value,edges[i][0])
        ans += edges[i][0]

print(ans-max_value)