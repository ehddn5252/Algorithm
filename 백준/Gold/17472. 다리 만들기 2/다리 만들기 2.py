from collections import deque

def find(u):
    if parent[u] == u:
        return u
    else:
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
        for i in range(len(parent)):
            if parent[i]==u:
                parent[i]=v
    else:
        parent[v] = u
        for i in range(len(parent)):
            if parent[i]==v:
                parent[i]=u
    check = True


parent = [i for i in range(6 + 1)]
l = []
n, m = map(int, input().split(" "))
visit = [[False for i in range(m)] for _ in range(n)]
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for i in range(n):
    l.append(list(map(int, input().split(" "))))



def BFS(input_i, input_j, island_number):
    q = deque([(input_i, input_j)])
    while q:
        now_i, now_j = q.popleft()
        for i in range(4):
            next_i = now_i + di[i]
            next_j = now_j + dj[i]
            if 0 <= next_i < n and 0 <= next_j < m:
                if l[next_i][next_j] == 1 and not visit[next_i][next_j]:
                    visit[next_i][next_j] = True
                    q.append((next_i, next_j))
                    l[next_i][next_j] = island_number


island_number = 1
for i in range(n):
    for j in range(m):
        if not visit[i][j] and l[i][j] == 1:
            visit[i][j] = True
            l[i][j] = island_number
            BFS(i, j, island_number)
            island_number += 1


def calc_distance(i1, j1, i2, j2):
    return abs(i1 - i2) + abs(j1 - j2) - 1


def route_check(i1, j1, i2, j2):
    if i1 > i2:
        i1, i2 = i2, i1
    if j1 > j2:
        j1, j2 = j2, j1
    if i1 == i2:
        for t in range(j1 + 1, j2):
            if l[i1][t] != 0:
                return False
    elif j1 == j2:
        for i in range(i1 + 1, i2):
            if l[i][j1] != 0:
                return False
    return True


new_q = []
for start_i in range(n):
    for start_j in range(m):
        if l[start_i][start_j] == 0: continue
        for end_i in range(n):
            for end_j in range(m):
                if l[start_i][start_j] != 0 and l[end_i][end_j] != 0 and l[start_i][start_j] != l[end_i][end_j]:
                    if start_i == end_i or start_j == end_j:
                        if route_check(start_i, start_j, end_i, end_j):
                            dis = calc_distance(start_i, start_j, end_i, end_j)
                            if dis >= 2:
                                new_q.append((dis, l[start_i][start_j], l[end_i][end_j]))

new_q = list(set(new_q))
new_q.sort()
ans = 0
check = False

for i in range(len(new_q)):
    merge(new_q[i][1], new_q[i][2])
    if check:
        ans += new_q[i][0]

first = parent[1]
for i in range(1, island_number):
    if first != parent[i]:
        ans = 0
if ans == 0:
    print(-1)
else:
    print(ans)
