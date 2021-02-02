# 1. nQueen은 줄마다 이동한다.
# 2. [] 안의 수가 row 값이 col이다 
global chessBoardRow
global N
answer=0

def canLocateQueen(row):
    for i in range(row):
        currentCol=chessBoardRow[row]
        comparedCol=chessBoardRow[i]
        if currentCol==comparedCol or abs(row-i)==abs(currentCol-comparedCol):
            return False
    return True

def nQueen(currentRow):
    global answer
    if currentRow==N:
        answer+=1
        return

    for row in range(N):
        chessBoardRow[currentRow]=row
        if canLocateQueen(currentRow):
            nQueen(currentRow+1)


if __name__ == "__main__":
    N = int(input())
    chessBoardRow=list(0 for i in range(N))

    nQueen(0)
    print(answer)

