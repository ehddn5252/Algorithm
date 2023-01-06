from collections import deque
import sys 
sys.setrecursionlimit(100000)


N = int(input())

l = [[] for _ in range(N + 1)]
cycle_num = -1
for i in range(N):
    a, b = map(int, input().split(" "))
    l[a].append(b)
    l[b].append(a)


def dfs(now_i, start_i, count):
    global cycle_num, cycle
    visit[now_i] = True
    for i in l[now_i]:
        if not visit[i]:
            dfs(i, start_i, count + 1)

        if count > 1 and i == start_i:
            cycle = True
            return


q = deque([])
station = [-1 for i in range(N + 1)]
for i in range(1, N + 1):
    visit = [False for i in range(N + 1)]
    cycle = False
    dfs(i, i, 0)
    if cycle:
        station[i] = 0
        q.append((i, 0))



visit = [False for i in range(N + 1)]
while q:
    node, value = q.popleft()
    for i in l[node]:
        if visit[i]:
            continue
        if station[i] != 0:
            visit[i] = True
            station[i] = value + 1
            q.append((i, value + 1))
        else:
            visit[i] = True
            q.append((i, value))
for i in range(1, N + 1):
    print(station[i], end=" ")
