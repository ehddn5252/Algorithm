# 작성일 : 20201202
# 작성자 : 김동우
# 문제명 : 체스판 다시 칠하기

# 문제 본문은 contents.md 참고 
# 문제 요약 : N x M사이즈의 판이 있다 이 판을 잘라 8 x 8 사이즈의 체스판을 만든다
#            체스판은 흰색 다음 검은색 이런 패턴이 있는데, 이 패턴에 맞게 체스판을 만들 때
#            가장 적게 칠해서 체스판을 만드는 경우는?

# 문제 해설 :
# 1. 체스판 칠하는 규칙은 col+row가 홀수인 것의 색과 col+row가 짝수인 것의 색이 달라야 한다
# 2. 체스판 칠하는 규칙에 맞게 두 경우 다 확인한다 (case1,case2)
# 3. 전체 보드중 8 x 8 사이즈를 한칸씩 옮기면서 다 확인해보고 규칙에 맞다면 case에 값을 +1하고 아니면 지나간다
# (+ 한번 8 x 8 을 돌때마다 case1과 case2를 0으로 초기화 해줘야 한다.)

# 시간 복잡도 O(64N^2)

def solution():
    N,_=map(int,input().split())
    chessBoard=[]
    for _ in range(N):
        chessBoard.append(input())

    ans=9999999
    case1=0
    case2=0
    for j in range(len(chessBoard)-7):
        for i in range(len(chessBoard[j])-7):
            for row in range(j,8+j):
                for col in range(i,8+i):
                    if(chessBoard[row][col]=='W' and (col+row)%2==0):
                        case1+=1
                    if(chessBoard[row][col]=='B' and (col+row)%2==1):
                        case1+=1
                    if(chessBoard[row][col]=='W' and (col+row)%2==1):
                        case2+=1
                    if(chessBoard[row][col]=='B' and (col+row)%2==0):
                        case2+=1
            
            if case2<ans:
                ans=case2
            if case1<ans:
                ans=case1
            case1=0
            case2=0

    print(ans)
            


if __name__ == "__main__":
    solution()