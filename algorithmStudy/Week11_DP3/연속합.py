import sys


def solution(inputedList):
    dp=[-1000]*100000
    dp[0]=inputedList[0]
    dp[1]=inputedList[1]
    maxValue=inputedList[0]
    for index in range(1,len(inputedList)):
        dp[index]= max(dp[index-1]+inputedList[index],inputedList[index])
        if maxValue<dp[index]:
            maxValue=dp[index]
    print(maxValue)


if __name__=="__main__":
    n=int(sys.stdin.readline())
    inputedList=list(map(int,sys.stdin.readline().split()))
    if n==1:
        print(inputedList[0])
    else:
        solution(inputedList)