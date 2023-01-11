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


check = False
V, E = map(int, input().split(" "))
edge = []

for i in range(E):
    a, b, c = map(int, input().split(" "))
    edge.append([c, a-1, b-1])
edge.sort()
parent = []
ans = 0
for i in range(V):
    parent.append(i)
for i in range(E):
    merge(edge[i][1], edge[i][2])
    if check:
        ans += edge[i][0]

print(ans)
