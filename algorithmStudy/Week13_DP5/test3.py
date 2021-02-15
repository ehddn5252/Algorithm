# 작성일자 : 20210212
# 문제명 : 내리막 길

# 문제 요약 :

# 문제 풀이 : 2차원 dp 배열을 사용해서 경우의 수를 누적시킨다. 여기서 맨 오른쪽과 맨 아랫줄은 바로 초기화를 시켜줘야 한다. 
# 근데 이렇게 하면 다른 결과에도 영향을 주기 때문에 옆 줄을 하나 더 늘려서 해야하나.. 
# 아니면 음..

from sys import stdin

moveX = [1,0,-1,0]
moveY = [0,1,0,-1]

def solution(mapList):
    global dp

    for rowIndex,row in enumerate(dp):
        for colIndex,_ in enumerate(row):
            if colIndex!=0 and mapList[rowIndex][colIndex]<mapList[rowIndex][colIndex-1]:
                dp[rowIndex][colIndex]+=dp[rowIndex][colIndex-1]
            if rowIndex!=0 and mapList[rowIndex][colIndex]<mapList[rowIndex-1][colIndex]:
                dp[rowIndex][colIndex]+=dp[rowIndex-1][colIndex]
            if colIndex!=len(row)-1 and mapList[rowIndex][colIndex]<mapList[rowIndex][colIndex+1]:
                dp[rowIndex][colIndex]+=dp[rowIndex][colIndex+1]
            if rowIndex!=len(dp)-1 and mapList[rowIndex][colIndex]<mapList[rowIndex+1][colIndex]:
                dp[rowIndex][colIndex]+=dp[rowIndex+1][colIndex]

    for i in dp:
        print(i)
    print(dp[-1][-1])

if __name__=="__main__":
    col,row1=map(int,stdin.readline().split())
    dp=[[-1]*row1 for i in range(col)]
    dp[0][0]=1
    mapList=[]
    for _ in range(col):
        mapList.append(list(map(int,stdin.readline().split())))
    solution(mapList)
