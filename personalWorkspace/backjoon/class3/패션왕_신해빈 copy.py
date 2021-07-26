# 작성일자 : 20210302
# 문제명 : 맥주 마시면서 걸어가기 백준 [9205]
import sys
import math


def solution():
    convenienceNum=int(sys.stdin.readline())
    beforeLocation=list(map(int,sys.stdin.readline().split()))
    convenienceList=[]
    for _ in range(convenienceNum):
        currentLocation=list(map(int,sys.stdin.readline().split()))
        distance=abs(currentLocation[0]-beforeLocation[0])+abs(currentLocation[1]-beforeLocation[1])
        if distance//50



if __name__=="__main__":
    testCase=int(sys.stdin.readline())
    for i in range(testCase):
        solution()