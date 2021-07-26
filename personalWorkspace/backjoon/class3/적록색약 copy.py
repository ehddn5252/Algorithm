# 작성일자 : 20210302
# 문제명 : 맥주 마시면서 걸어가기 백준 [9205]
import sys
import math

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs1(y,x):
    global mapSize
    color=redGreenBlueMap[y][x]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        print(mapSize)
        if nx<0 or nx>=mapSize or ny<0 or ny>=mapSize:
            continue
        if redGreenBlueMap[ny][nx]==color:
            redGreenBlueMap[ny][nx]='x'
            dfs1(ny,nx)


def dfs2(y,x):
    global mapSize
    color=redBlueMap[y][x]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=mapSize or ny<0 or ny>=mapSize:
            continue
        if redBlueMap[ny][nx]==color:
            redBlueMap[ny][nx]='x'
            dfs2(ny,nx)


def solution():
    global redBlueMap, mapSize
    redBlueMap=redGreenBlueMap[:]

    # RGB지도를 RB지도로 바꿈
    for rowIndex,row in enumerate(redBlueMap):
        for colIndex,_ in enumerate(row):
            if redBlueMap[rowIndex][colIndex]=='G':
                redBlueMap[rowIndex][colIndex]='R'

    for i in range(mapSize):
        for j in range(mapSize):
            if dfs1(i,j)!='x':
                print(f'{i},{j}')
                dfs1(i,j)
                answer1+=1
            if dfs2(i,j)!='x':
                dfs2(i,j)
                answer2+=1
    
    print(answer1)
    print(answer2)


if __name__=="__main__":
    global mapSize, answer1,answer2,redGreenBlueMap
    answer=0
    mapSize=int(sys.stdin.readline())
    redGreenBlueMap=[]
    for i in range(mapSize):
        readline1=list(map(str,sys.stdin.readline()))
        redGreenBlueMap.append(readline1)
    solution()
