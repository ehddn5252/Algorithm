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

while True:
    edge = []
    check = False
    V, E = map(int, input().split(" "))
    if V==0 and E==0:
        break
    ans = 0
    for i in range(E):
        a, b, c = map(int, input().split(" "))
        ans += c
        edge.append([c, a, b])


    edge.sort()
    parent = []
    for i in range(V):
        parent.append(i)
    for i in range(E):
        merge(edge[i][1], edge[i][2])
        if check:
            ans -= edge[i][0]
    print(ans)
