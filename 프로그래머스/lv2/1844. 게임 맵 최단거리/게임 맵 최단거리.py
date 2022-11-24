"""
요구사항
1. 시작점에서 상대 진영까지 가야한다.
2. 가는 길이 막혀 있다면 -1을 return 한다.

풀이
나는 1.1 자리에 있다. 상대방은 n,m 자리에 있음
벽은 0 길은 1이다. BFS 로 길을 탐색해야 한다.

"""
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(maps):
    return BFS(maps)


def BFS(maps):
    queue = deque([[0, 0, 1]])
    visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visit[0][0] = 1
    min_value = 99999
    while queue:
        popped = queue.popleft()
        next_value = popped[2]
        if min_value < next_value:
            continue
        for i in range(4):
            next_x = popped[0] + dx[i]
            next_y = popped[1] + dy[i]

            if next_x >= 0 and next_x < len(maps[0]) and next_y >= 0 and next_y < len(maps):
                if maps[next_y][next_x] == 0:
                    continue
                if visit[next_y][next_x] == 0 and maps[next_y][next_x] == 1:
                    queue.append([next_x, next_y, next_value + 1])
                    visit[next_y][next_x] = next_value + 1
                    if next_x == len(maps[0]) - 1 and next_y == len(maps) - 1:
                        if min_value > visit[next_y][next_x]:
                            min_value = visit[next_y][next_x]
    return visit[-1][-1] if visit[-1][-1] != 0 else -1
