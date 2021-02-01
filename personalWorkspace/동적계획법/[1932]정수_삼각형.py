import sys

# 작성일자 20210201
# 문제명 : 백준 1932 정수 삼각형
# 문제 풀이 :
# 1. 입력 삼각형의 값을 가지는 dp배열을 만든다.
# 2. 왼쪽 위 또는 오른쪽 위에 있는 수와 지금 dp를 비교해서 더 큰 값을 저장한다
# (dp[rowIndex][colIndex]=max(dp[rowIndex-1][colIndex],dp[rowIndex-1][colIndex-1])+dp[rowIndex][colIndex])
# out of index가 나지 않게 예외 사항을 정해준다.

def solution(triangle):
    dp=triangle[:]

    for rowIndex,row in enumerate(triangle):
        for colIndex,_ in enumerate(row):
            if rowIndex==0: continue
            if colIndex==0:
                dp[rowIndex][colIndex]=dp[rowIndex-1][colIndex]+dp[rowIndex][colIndex]
            elif colIndex==rowIndex:
                dp[rowIndex][colIndex]=dp[rowIndex-1][colIndex-1]+dp[rowIndex][colIndex]
            else:
                dp[rowIndex][colIndex]=max(dp[rowIndex-1][colIndex],dp[rowIndex-1][colIndex-1])+dp[rowIndex][colIndex]

    print(max(dp[-1]))



if __name__=="__main__":
    n=int(sys.stdin.readline())
    triangle=[]
    for i in range(n):
        triangle.append(list(map(int,sys.stdin.readline().split())))
    if n==1:
        print(triangle[0][0])
    else:
        solution(triangle)