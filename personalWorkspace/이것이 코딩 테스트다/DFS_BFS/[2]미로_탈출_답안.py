# 작성일자 : 20210205
# 문제명 : 미로 탈출
# 문제 요약 : 
# 나는 지금 (1,1)에 있다. 미로를 탈출해야 한다. 괴물은 0으로 괴물은 만나면 안된다. 1인 칸은 이동 가능하다. 
# 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라

from collections import deque
# N,M을 공백으로 구분하여 입력받기 
n,m = map(int,input().split())
# 2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]

# BFS 소스코드 구현
def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx= x+ dx[i]
            ny= y+ dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0 :
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1 :
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))