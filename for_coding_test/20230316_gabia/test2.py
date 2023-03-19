# 못품..

N, M = map(int, input().split(" "))

map1 = []

for _ in range(N):
    tmp_input = input()
    map1.append(tmp_input)

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
visit = [[0 for _ in range(M)] for _ in range(N)]
ans = 0
from collections import deque

q = deque([])

for i in range(N):
    for j in range(M):
        visit = [[0 for _ in range(M)] for _ in range(N)]
        if map1[i][j] == "L":
            visit[i][j] = 1
            q.append((i, j))
            last_i, last_j = -1, -1
            while q:
                popped_i, popped_j = q.popleft()
                last_i, last_j = popped_i, popped_j
                for d_index in range(4):
                    next_i = popped_i + di[d_index]
                    next_j = popped_j + dj[d_index]
                    if next_j >= 0 and next_j < M and next_i >= 0 and next_i < N and visit[next_i][next_j] == 0 and \
                            map1[next_i][next_j] == "L":
                        visit[next_i][next_j] = 1
                        q.append((next_i, next_j))
            q.append((last_i, last_j, 0))
            visit[last_i][last_j] = 2
            max_time = 0
            while q:
                popped_i, popped_j, time = q.popleft()
                if max_time < time:
                    max_time = time
                for d_index in range(4):
                    next_i = popped_i + di[d_index]
                    next_j = popped_j + dj[d_index]
                    if next_j >= 0 and next_j < M and next_i >= 0 and next_i < N and map1[next_i][next_j] == "L" and \
                            visit[next_i][next_j] == 1:
                        visit[next_i][next_j] = 2
                        q.append((next_i, next_j, time + 1))
            if ans < max_time:
                ans = max_time

print(ans)