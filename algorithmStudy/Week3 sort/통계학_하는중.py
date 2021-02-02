import sys
# https://www.acmicpc.net/problem/2108


# 최빈값 구하는 방법
# 해시로
def getMode(numberList):
    maxValue=-1
    tmpMax=0
    count=-1
    for i in numberList:
        if numberList[i-1]==numberList[i]:
            tmpMax+=1
        else:
            tmpMax=0
        if maxValue<tmpMax:
            maxValue=tmpMax
            mode=i
            count=0
        elif maxValue==tmpMax and count==0:
            mode=i
            count=1
    return mode
    


def solution(numberList):
    arithmeticMean=round(sum(numberList)/N)
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
    N= int(sys.stdin.readline())
    numberList=[]
    for i in range(N):
        numberList.append(int(sys.stdin.readline()))
    solution(numberList)
