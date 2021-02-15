# 작성 일자 : 20210215
# 문제명 : 유기농 배추 (백준 1012)
# 문제 요약 : field에 배추가 있는 곳이 주어진다. 
# 배추가 있는 지역별로 하나씩 배추흰지렁이를 넣는다.
# 배추흰지렁이는 몇마리 필요한가?
# 여기서 지역은 배추가 연속적으로 있는 곳 기준으로 한 지역이 된다. 

# 문제 풀이 : 이건 DFS의 대표적인 문제이다.
# 4방향에서 연결되어 있는 지 확인하는 배열 dx ,dy를 만든다.
# 모든 위치에 대해서 그 위치의 값이 1(배추가 있는 우치)인지 확인한다.
# 만약 1이라면 dfs로 들어가 상하좌우를 확인해 배추가 있는 지 확인하고 있다면 그 값을 -1로 대입한다.
# 이렇게 하면 최초로 배추를 발견했을 때만 count하고 나머지 경우는 count하지 않아 구역의 수를 구할 수 있다.  
from sys import stdin
import sys
sys.setrecursionlimit(10000)

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(y,x):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=M or ny<0 or ny>=N:
            continue
        if field[ny][nx]==1:
            field[ny][nx]=-1
            dfs(ny,nx)

if __name__=="__main__":
    testCase=int(stdin.readline())
    for _ in range(testCase):
        cnt=0
        # 가로길이, 세로길이, 배추 위치
        M,N,K=map(int,stdin.readline().split())
        field=[[0]*M for _ in range(N)]
        for i in range(K):
            cabbageLocationX,cabbageLocationY=map(int,stdin.readline().split())
            field[cabbageLocationY][cabbageLocationX]=1

        for i in range(N):
            for j in range(M):
                if field[i][j]>0:
                    dfs(i,j)
                    cnt+=1
        print(cnt)