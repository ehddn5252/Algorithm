import sys
import math
# https://www.acmicpc.net/problem/2108

def getMode(numberList):
    tmpMax=1
    maxValue=1
    mode=0
    for i in range(numberList):
        if numberList[i]==numberList[i+1]:
            tmpMax+=1
        else:
            tmpMax=0
        if maxValue<tmpMax:
            tmpMax=maxValue
            mode=numberList[i]
    return mode

def solution(numberList):
    arithmeticMean=sum(numberList)/N
    numberList.sort()
    median=numberList[N//2]
    # 최빈값을 구해야 한다. 최빈값은 중복값이 가장 많이 나오는 값
    rangeValue=numberList[-1]-numberList[0]
    mode=getMode(numberList)
    
    
        
    print(arithmeticMean)
    print(median)
    print(mode)
    print(rangeValue)

if __name__ == "__main__":
    N= int(sys.stdin.readline().strip())
    numberList=[]
    for i in range(N):
        numberList.append(int(sys.stdin.readline().strip()))
    solution(numberList)
