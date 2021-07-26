# 작성일 : 20210318
# 문제명 : 경주로 건설
# 문제 요약 : 지도가 있을 때 장애물을 피해서0,0에서 N-1,N-1 가는 최소 비용 구하기
#            단 직진은 100원 커브는 500원이다.

# 문제 풀이 : 뒤로가는 커브가 있어서 dp를 사용해야할듯


def solution(board):
    length=len(board)
    dp=[[0]*length for i in range(length)]
    dp[0][0]=100
    for index in range(1,length):
        dp[0][index]=dp[0][index-1]+100
        dp[index][0]=dp[index-1][0]+100

    for colIndex,colValue in enumerate(board):
        for rowIndex,rowValue in enumerate(colValue):
            if board[colIndex][rowIndex]==1:
                dp[colIndex][rowIndex]=0

    for colIndex,colValue in enumerate(board):
        for rowIndex,rowValue in enumerate(colValue):
            if dp[0][rowIndex-1]==0:
                dp[0][rowIndex]=0
            if dp[colIndex-1][0]==0:
                dp[colIndex][0]=0
            

    for colIndex,colValue in enumerate(board):
        for rowIndex,rowValue in enumerate(colValue):
            if colIndex!=0 and rowIndex!=0:
                if dp[colIndex-1][rowIndex]!=1 and dp[colIndex][rowIndex-1]!=1 and dp[colIndex-1][rowIndex-1]!=0:
                    dp[colIndex][rowIndex]=dp[colIndex-1][rowIndex-1]+600
                elif dp[colIndex-1][rowIndex-1]==0:
                    dp[colIndex][rowIndex]=max(dp[colIndex][rowIndex-1],dp[colIndex-1][rowIndex])+100
    print(dp)
    return 0



if __name__=="__main__":
    board1=[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
    

    solution(board1)