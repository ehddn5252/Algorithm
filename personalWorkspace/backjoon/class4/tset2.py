# 작성 일자 : 20210313
# 문제 명 : 연구소
# 문제 요약 : 
import sys


def solution(inputList):
    for row in inputList:
        for col in row:


if __name__=="__main__":
    row,col=map(int,sys.stdin.readline().split())
    mapList=[]
    for i in range(row):
        inputList=list(map(int,sys.stdin.readline().split()))
        mapList.append(inputList)
        solution(inputList)
