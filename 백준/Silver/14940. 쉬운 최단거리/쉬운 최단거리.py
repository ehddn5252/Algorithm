n, m = map(int, input().split(" "))
l = []
visit = [[False for _ in range(m)] for _ in range(m)]
import sys

start_position = []
for i in range(n):
    inner_l = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(m):
        if inner_l[j] == 2:
            start_position = (i, j, 0)
    l.append(inner_l)

"""
1. 시작 위치에서 bfs로 퍼져나간다.
"""

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

q = [start_position]
l[start_position[0]][start_position[1]] = 0
visit[start_position[0]][start_position[1]] = True
q = deque(q)
while q:
    popped_i, popped_j, distance = q.popleft()
    for i in range(4):
        next_i = popped_i + di[i]
        next_j = popped_j + dj[i]
        if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m \
                or visit[next_i][next_j] \
                or l[next_i][next_j] == 0: continue
        visit[next_i][next_j] = True
        l[next_i][next_j] = distance + 1
        q.append((next_i, next_j, distance + 1))

for i in range(n):
    for j in range(m):
        if not visit[i][j] and l[i][j] != 0:
            l[i][j] = -1

for i in range(n):
    for j in range(m):
        if j == m - 1:
            print(l[i][j], end="")
        else:
            print(l[i][j], end=" ")
    print()
