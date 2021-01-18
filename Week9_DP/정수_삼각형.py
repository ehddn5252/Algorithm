def solution(triangle):
    answer = 0
    dp=triangle[:]
    for rowIndex,rowValue in enumerate(dp):
        if rowIndex==0: continue
        for colIndex,colValue in enumerate(rowValue):
            if colIndex==0:
                dp[rowIndex][colIndex]=dp[rowIndex][colIndex]+dp[rowIndex-1][colIndex]
            elif colIndex>0 and colIndex<len(rowValue)-1:
                dp[rowIndex][colIndex]= max(dp[rowIndex][colIndex]+dp[rowIndex-1][colIndex],dp[rowIndex][colIndex]+dp[rowIndex-1][colIndex-1])
            else:
                dp[rowIndex][colIndex]= dp[rowIndex][colIndex]+dp[rowIndex-1][colIndex-1]


    for col,rowValue in enumerate(dp[-1]):
        if answer<dp[-1][col]:
            answer=dp[-1][col]
    return answer

if __name__ == "__main__":
    triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    solution(triangle)