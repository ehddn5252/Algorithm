from pprint import pprint
from collections import deque

answer = 200
# for input setting and variable setting
n = int(input())
map1 = [list(map(int, input().split(" "))) for _ in range(n)]
visit = [[0 for i in range(n)] for _ in range(n)]
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

island_index = -1
q2 = deque([])

# BFS 로 맨 처음 다른섬 체크하는 세팅하기
def BFS(row_index, col_index, island_index):
    q = deque([[row_index, col_index]])
    q2.append([row_index, col_index, island_index])
    visit[row_index][col_index] = island_index
    while q:
        popped = q.popleft()

        # 4방향 검색
        for i in range(4):
            next_r = popped[0] + dr[i]
            next_c = popped[1] + dc[i]
            if next_r >= 0 and next_r < n and next_c >= 0 and next_c < n:
                if map1[next_r][next_c] == 1 and visit[next_r][next_c] == 0:
                    visit[next_r][next_c] = island_index
                    q.append([next_r, next_c])
                    # 이후 섬끼리 최단 거리 찾기 위한 queue r,c,섬번호, 이동거리
                    q2.append([next_r, next_c, island_index])


def BFS2(row_index, col_index, island_index):
    global answer
    q = deque([[row_index, col_index, 0]])

    while q:
        popped = q.popleft()
        if answer <= popped[2]:
            continue
        for i in range(4):
            next_r = popped[0] + dr[i]
            next_c = popped[1] + dc[i]
            if next_r >= 0 and next_r < n and next_c >= 0 and next_c < n:
                if visit[next_r][next_c] == 0 or visit[next_r][next_c] > popped[2]+1:
                    visit[next_r][next_c] = popped[2]+1
                    q.append([next_r, next_c, popped[2] + 1])
                elif visit[next_r][next_c] != island_index and map1[next_r][next_c] == 1:
                    answer = min(answer, popped[2])

for row_index in range(n):
    for col_index in range(n):
        if visit[row_index][col_index] == 0 and map1[row_index][col_index] == 1:
            BFS(row_index, col_index, island_index)
            island_index -= 1



while q2:
    popped = q2.popleft()
    BFS2(popped[0],popped[1],popped[2])

print(answer)



