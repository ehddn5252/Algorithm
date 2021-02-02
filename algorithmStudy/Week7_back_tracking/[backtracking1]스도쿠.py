global endFlag
global sdokuList
endFlag=False

# 스도쿠가 되는 조건 확인하는 코드
def check(row,col,compareValue):
    for i in range(1,9):
        if sdokuList[row][i]==compareValue or sdokuList[i][col]==compareValue:
            return False
    return True

def sdoku():
    global endFlag
    if endFlag==True:
        return
    for row in range(0,9):
        for col in range(0,9):
            if sdokuList[row][col]==0:
                for compareValue in range(1,10):
                    if check(row,col,compareValue)==True:
                        sdokuList[row][col]=compareValue
                        sdoku()
                        #sdokuList[row][col]=0
                return
    endFlag==True
    


if __name__ == "__main__":
    global sdokuList
    # 데이터 처리
    sdokuList=[[] for _ in range(9)]
    for i in range(9):
        num=map(int,input().split())
        for j in num:
            sdokuList[i].append(j)
    # 데이터 처리 끝
    sdoku()
    # 출력
    ansStr=""
    for row in sdokuList:
        for col in row:
            ansStr+=str(col)+" "
        ansStr+="\n"
    print(ansStr)