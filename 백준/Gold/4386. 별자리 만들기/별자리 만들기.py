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
    parent[u] = v
    check = True


edge = []
check = False
V = int(input())
l = []
ans = 0
import math


def distance(a, b):
    return int(abs(math.sqrt((l[a][0] - l[b][0]) ** 2 + (l[a][1] - l[b][1]) ** 2))*100)/100


for i in range(V):
    a, b = map(float, input().split(" "))
    l.append([a, b])

for i in range(len(l)):
    for j in range(i, len(l)):
        if i == j:
            continue
        edge.append((distance(i, j), i, j))

edge.sort()
parent = []
for i in range(V):
    parent.append(i)
for i in range(len(edge)):
    merge(edge[i][1], edge[i][2])
    if check:
        ans += edge[i][0]
print(ans)
