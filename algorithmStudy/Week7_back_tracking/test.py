

# 문제 해설 :
# 1. 만약 끝까지 갔다면 answer+=1
# 2. 아니라면 n까지 count해서 리스트에 넣는다.
# 3. 현재 위치에 퀸을 놓을 수 있는 지 확인한다.
# 4. 넣을 수 없다면 return
# 5. 넣을 수 있다면

global answer
answer = 0




def canLocateQueen(queenLocation):
    global N
    candidate = list(range(queenLocation))
    for i in range(N):
        chessBoard[queenLocation]=i
        if chessBoard[i] in candidate:
            candidate.remove(chessBoard[i])

        i == chessBoard[queenLocation] or abs(i-queenLocation) == abs(chessBoard[i]-chessBoard[queenLocation]):
            return False
    return True


def N_Queen(start):
    global answer, N
    if start == N:
        answer += 1
        return
    for i in range(N):
        if canLocateQueen(i):
            N_Queen(chessBoard, start+1)

def solution():
    global N
    N=int(input())
    N_Queen(0)




if __name__ == "__main__":
    global N
    global chessBoard[15]

    N = int(input())
    solution()
    print(answer)

