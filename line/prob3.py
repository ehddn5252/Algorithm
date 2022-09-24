from typing import List
from collections import deque

fire_d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
ice_d = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def BFS(map1, location, m, add_num, n):
    x, y = location[0] - 1, location[1] - 1
    visit = [[False for _ in range(n)] for _ in range(n)]
    visit[x][y] = True
    q = [[x, y]]
    q = deque(q)

    if add_num == 1:
        d = fire_d
    else:
        d = ice_d

    minute = 0
    q_count = 1
    while minute < m:
        before_q_count = q_count
        for _ in range(q_count):
            x, y = q.popleft()
            for i in range(len(d)):
                new_x = d[i][0] + x
                new_y = d[i][1] + y
                if new_x >= 0 and new_x < n and new_y >= 0 and new_y < n:
                    if not visit[new_x][new_y]:
                        visit[new_x][new_y] = True
                        q.append([new_x, new_y])
                        q_count += 1
        for i in range(n):
            for j in range(n):
                if visit[i][j]:
                    map1[i][j] += add_num
        minute += 1
        q_count = q_count - before_q_count
    return map1


def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    '''
    n x n 크기 map
    m 분 후의 상태 확인
    fires 는 불 x,y좌표
    ices 는 얼음 x,y좌표
    '''
    # map init 불과 얼음 개수
    answer = [[0 for _ in range(n)] for _ in range(n)]

    for fire_location in fires:
        answer = BFS(answer, fire_location, m, 1, n)
    for ice_location in ices:
        answer = BFS(answer, ice_location, m, -1, n)
    return answer


n = 3
m = 2
fires = [[1, 1]]
ices = [[3, 3]]

solution(n, m, fires, ices)
