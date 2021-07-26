# 작성일자 : 20210302
# 문제명 : 미로 탐색
# 문제 요약: 미로 탐색

from sys import stdin

answerList=[]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(x,y):
    queue=[]
    

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

    if [nx,ny] not in visited:
        queue.append([nx,ny])

if __name__=="__main__":
    row,col=map(int,stdin.readline().split())
    mapList=[]
    visited=[]
    for i in range(row):
        rowList=list(map(int,stdin.readline().strip()))
        mapList.append(rowList)
        visited.append([0]*col)
    queue=[[0,0]]

    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=row or ny<0 or ny>=col:
                continue

            if mapList[nx][ny]==0:
                continue
            if visited[nx][ny]==0:
                visited[nx][ny]=1
                if mapList[nx][ny]!=1:
                    mapList[nx][ny]=min(mapList[x][y]+1,mapList[nx][ny])
                else:
                    mapList[nx][ny]=mapList[x][y]+1
                queue.append([nx,ny])
    print(mapList[-1][-1])
