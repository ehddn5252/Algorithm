# 작성일자 : 20210302
# 문제명 : 적록 색약 백준 [10026]
# deep copy를 하지 않으면 참조만 될 뿐이다.
# dfs를 사용한다.
# dfs  
# 1. 모든 경우의 수를 다 확인한다.
# 2. 그 경우의 dx=[-1,0,1,0] dy = [0,1,0,-1] 로 설정해서 x= x+dx, y=y+dy로 설정 
# 3. 그 경우가 visit인지 확인하고 visit이면 통과 아니면 재귀 호출 
import sys
import math
import copy
sys.setrecursionlimit(10000)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs1(y,x,color):
    global mapSize, redGreenBlueMap
    redGreenBlueMap[y][x]='x'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=mapSize or ny<0 or ny>=mapSize:
            continue
        if color != 'x' and redGreenBlueMap[ny][nx]==color:
            redGreenBlueMap[ny][nx]='x'
            dfs1(ny,nx,color)


def dfs2(y,x,color):
    global mapSize, redBlueMap
    redBlueMap[y][x]='x'
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=mapSize or ny<0 or ny>=mapSize:
            continue
        if color != 'x' and redBlueMap[ny][nx]==color:
            redBlueMap[ny][nx]='x'
            dfs2(ny,nx,color)


def solution():
    global redBlueMap
    answer1=0
    answer2=0
    redBlueMap=copy.deepcopy(redGreenBlueMap)

    # RGB지도를 RB지도로 바꿈
    for rowIndex in range(mapSize):
        for colIndex in range(mapSize):
            if redBlueMap[rowIndex][colIndex]=='G':
                redBlueMap[rowIndex][colIndex]='R'
    for i in range(mapSize):
        for j in range(mapSize):
            if redGreenBlueMap[i][j]!='x':
                color1=redGreenBlueMap[i][j]
                dfs1(i,j,color1)
                answer1+=1
            if redBlueMap[i][j]!='x':
                color2=redBlueMap[i][j]
                dfs2(i,j,color2)
                answer2+=1

    print(f'{answer1} {answer2}')


mapSize=int(sys.stdin.readline())
global redGreenBlueMap
redGreenBlueMap=[]
for i in range(mapSize):
    readline1=list(map(str,sys.stdin.readline().strip()))
    redGreenBlueMap.append(readline1)
try:
    solution()
except:
    print(f'error')
