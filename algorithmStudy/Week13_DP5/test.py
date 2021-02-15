from sys import stdin

def dfs(x:int,y:int)-> int:
    if x==col-1 and y==row-1:
        return 1
    rtn=0
    for i in range(4):
        nextX=x+moveX[i]
        nextY=y+moveY[i]
        if 0<= nextX< col and 0<=nextY<row and (mapList[nextX][nextY]>mapList[x][y]):
            if dp[nextX][nextY]>=0:
                rtn+=dp[nextX][nextY]
            else:
                rtn+=dfs(nextX,nextY)
    dp[x][y]+=dfs(nextX,nextY)
    return rtn


col,row=map(int,stdin.readline().split())
dp=[[-1]*row for i in range(col)]
mapList=[]

for _ in range(col):
    mapList.append(list(map(int,stdin.readline().split())))

moveX=[1,-1,0,0]
moveY=[0,0,1,-1]
print(dfs(col-1,row-1))
print(dp)