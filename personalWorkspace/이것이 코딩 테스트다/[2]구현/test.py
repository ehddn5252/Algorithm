# 작성일자 : 20210204
# 문제명 : 게임 개발
# 문제 요약 :
# 나이트는
#
import sys
'''

def solution():
    



if __name__=="__main__":
    rowSize,colSize= map(int,sys.stdin.readline().split())
    locationRow,locationCol,direction = map(int,sys.stdin.readline().split())
    mapList=[]
    for i in range(rowSize):
        colList=list(map(int,sys.stdin.readline().split()))
        mapList.append(colList)
    move=[(1,0),(0,-1),(0,1),(-1,0)]# 북 서 남 동
    userLocation=[locationRow,locationCol,direction]
    while True:
        mapList[userLocation[0]][userLocation[1]]=-1
        if mapList[userLocation[0] + move[direction%4][0]][userLocation[1] + move[direction%4][1]]==1:
            userLocation[0] = userLocation[0] + move[direction%4][0]
            userLocation[1] = userLocation[1] + move[direction%4][1]
        elif 
'''