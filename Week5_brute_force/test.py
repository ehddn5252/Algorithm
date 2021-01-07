# 작성일 : 20201202
# 작성자 : 김동우
# 문제명 : 체스판 다시 칠하기
# 문제 요약 :
#  
# 문제 본문은 contents.md 참고 

# 문제 해설 : 



def solution():
    _,M=map(int,input().split())
    chessBoard=[]
    for _ in range(M):
        chessBoard.append(input())


    for j in range(len(chessBoard)):
        for i in range(len(chessBoard)):
            print(chessBoard[i][j])
    '''
    ans=9999999
    for j in range(len(chessBoard)-8):
        for i in range(len(chessBoard[row])-8):
            for row in range(j,8+j):
                for col in range(i,8+i):
                    if(chessBoard[col][row]=='W' and (col+row)%2==0):
                        case1+=1
                    if(chessBoard[col][row]=='W' and (col+row)%2==1):
                        case2+=1
                    if(chessBoard[col][row]=='B' and (col+row)%2==0):
                        case1+=1
                    if(chessBoard[col][row]=='B' and (col+row)%2==1):
                        case2+=1
            if case2<ans:
                ans=case2
            if case1<ans:
                ans=case1
                case1=0
                case2=0
    '''
    #print(ans)
            


if __name__ == "__main__":
    solution()