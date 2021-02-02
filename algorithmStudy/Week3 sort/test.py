import sys
# https://www.acmicpc.net/problem/2108


# 최빈값 구하는 방법
# 해시로
def getMode(numberList):
    maxValue=0
    tmpMax=0
    setNumberList=set(numberList)
    setNumberList=list(setNumberList)
    for i in setNumberList:
        tmpMax=numberList.count(i)
        if maxValue<tmpMax:
            maxValue=tmpMax
    modeList=[]
    for i in setNumberList:
        tmpMax=numberList.count(i)
        if maxValue==tmpMax:
            modeList.append(i)

    modeList.sort()
    if len(modeList)>=2:
        return modeList[1]
    else:
        return modeList[0]


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
    N= int(sys.stdin.readline().strip())
    numberList=[]
    for i in range(N):
        numberList.append(int(sys.stdin.readline().strip()))
    solution(numberList)
