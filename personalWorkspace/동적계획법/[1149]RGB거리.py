# 작성일자 : 20210201
# 문제명 : 백준 [1149]RGB거리
# 문제 풀이 : RGBList를 받았을 때 색마다 최대값을 저장하는 dp를 만들면 된다.

import sys



def solution(RGBList):
    
    for index in range(len(RGBList)):
        if index==0:continue
        RGBList[index][0]=min(RGBList[index-1][1],RGBList[index-1][2])+RGBList[index][0]
        RGBList[index][1]=min(RGBList[index-1][0],RGBList[index-1][2])+RGBList[index][1]
        RGBList[index][2]=min(RGBList[index-1][0],RGBList[index-1][1])+RGBList[index][2]
    
    print(min(RGBList[-1]))
        
        

if __name__=="__main__":
    n= int(sys.stdin.readline())
    RGBList=[]
    for i in range(n):
        RGBList.append(list(map(int,sys.stdin.readline().split())))
    if n==1:
        print(min(RGBList[0]))
    else:
        solution(RGBList)

    