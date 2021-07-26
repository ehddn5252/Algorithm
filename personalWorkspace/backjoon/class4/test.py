# 작성일자 : 20210217
# 문제명 : 스티커
# 문제 풀이 : 그냥 보면 DP가 떠오를 것이다.
# 맞다. DP로 푼다 점화식을 구해보자.
# dp[i]=max(dp[i-1][j-1]+dp[i][j],dp[i-1][j],dp[i][j-1]) 

from sys import stdin

def solution(stickerList):
    dp=stickerList[:]
    for colIndex,colValue in enumerate(dp):
        for rowIndex,_ in enumerate(colValue):
            if colIndex==0:
                continue
            if rowIndex==0:
                continue
            dp[colIndex][rowIndex]=max(dp[colIndex-1][rowIndex-1]+dp[colIndex][rowIndex],dp[colIndex-1][rowIndex]+dp[colIndex][rowIndex-1])


if __name__=="__main__":
    testcase=int(stdin.readline())

    for i in range(testcase):
        length=int(stdin.readline())
        stickerList1=list(map(int,stdin.readline().split()))
        stickerList2=list(map(int,stdin.readline().split()))
        stickerList=[]
        stickerList=[stickerList1,stickerList2]
        solution(stickerList)
