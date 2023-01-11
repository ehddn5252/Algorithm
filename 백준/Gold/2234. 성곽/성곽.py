from pprint import pprint
from copy import deepcopy

N, M = map(int, input().split(" "))
l = []
PATH = -1
WALL = -2
ROOM = 0
basic_setting = [WALL for i in range(N * 2 + 1)]
l.append(deepcopy(basic_setting))
for i in range(M):
    tmp = list(map(int, input().split(" ")))
    new_tmp = [WALL]
    for j in range(N):
        new_tmp.append(tmp[j])
        new_tmp.append(WALL)
    l.append(new_tmp)
    l.append(deepcopy(basic_setting))
new_M = len(l)
new_N = len(l[0])
for i in range(new_M):
    for j in range(new_N):

        if l[i][j] >= 0:
            if l[i][j] >= 8:
                l[i][j] -= 8
                l[i + 1][j] = WALL
            elif 0 <= l[i][j] < 8:
                l[i + 1][j] = PATH

            if l[i][j] >= 4:
                l[i][j] -= 4
                l[i][j + 1] = WALL
            elif 0 <= l[i][j] < 4:
                l[i][j + 1] = PATH

            if l[i][j] >= 2:
                l[i][j] -= 2
                l[i - 1][j] = WALL
            elif 0 <= l[i][j] < 2:
                l[i - 1][j] = PATH

            if l[i][j] >= 1:
                l[i][j] -= 1
                l[i][j - 1] = WALL
            elif l[i][j] == 0:
                l[i][j - 1] = PATH
visit = [[0 for i in range(new_N)] for j in range(new_M)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

from collections import deque


def bfs(input_i, input_j, room_number):
    global room_area_max

    q = deque([(input_i, input_j)])
    count = 1
    while q:
        now_i, now_j = q.popleft()
        if count > room_area_max:
            room_area_max = count
        for i in range(4):
            next_i = now_i + dx[i]
            next_j = now_j + dy[i]

            if next_i < new_M and next_i >= 0 and next_j >= 0 and next_j < new_N:
                if visit[next_i][next_j] == 0 and l[next_i][next_j] != WALL:
                    visit[next_i][next_j] = room_number
                    if l[next_i][next_j] == ROOM:
                        count += 1
                        q.append((next_i, next_j))
                    else:
                        q.append((next_i, next_j))
    return count


room_number = 0
room_area_max = 1
case_room_area_max = 1

visit_2 = [0]
for i in range(new_M):
    for j in range(new_N):
        if l[i][j] == ROOM and not visit[i][j]:
            room_number += 1
            visit[i][j] = room_number
            visit_2.append(bfs(i, j, room_number))

d2x = [-2, 2, 0, 0]
d2y = [0, 0, -2, 2]
for i in range(1, new_M - 1):
    for j in range(1, new_N - 1):
        if l[i][j] == ROOM:
            for k in range(4):
                next_i = i + d2x[k]
                next_j = j + d2y[k]
                if next_i < new_M and next_i >= 0 and next_j >= 0 and next_j < new_N and l[next_i][next_j]==ROOM:
                    if visit[i][j] != visit[next_i][next_j]:
                        case_room_area_max = max(case_room_area_max,
                                                 visit_2[visit[i][j]] + visit_2[visit[next_i][next_j]])

print(room_number)
print(room_area_max)
print(case_room_area_max)
