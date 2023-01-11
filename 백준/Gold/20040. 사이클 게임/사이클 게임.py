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
    if u<v:
        parent[v]=u
    else:
        parent[u]=v
    check = True


check = False
V, E = map(int, input().split(" "))

parent = []
for i in range(V):
    parent.append(i)
ans = 0
for i in range(E):
    a, b = map(int, input().split(" "))
    merge(a, b)
    if not check:
        ans = i+1
        break
print(ans)
