# 문제명 : 음료수 얼려 먹기 답안
# 문제 요약 : N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라
# 

# N,M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <=-1 or x>=n or y <=-1 or y>=m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        graph[x][y]=1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j)==True:
            result+=1

print(f'{result}')
