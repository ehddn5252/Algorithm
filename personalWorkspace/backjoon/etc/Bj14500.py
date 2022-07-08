row_num, col_num = map(int, input().split(" "))

map1 = [list(map(int, input().split(" "))) for i in range(row_num)]

answer = 0

def long1(r, c):
    # 열렬로 되어있는 직사각형,하늘색
    global answer
    if r + 3 < row_num:
        answer = max(answer, map1[r][c] + map1[r + 1][c] + map1[r + 2][c] + map1[r + 3][c])
    if c + 3 < col_num:
        answer = max(answer, map1[r][c] + map1[r][c + 1] + map1[r][c + 2] + map1[r][c + 3])


def square(r, c):
    global answer
    if r + 1 < row_num and c + 1 < col_num:
        answer = max(answer, map1[r][c] + map1[r][c + 1] + map1[r + 1][c] + map1[r + 1][c + 1])


def type1(r, c):
    # 가운데 튀어나와 있는 모양, 분홍색
    global answer
    if r + 1 < row_num and c + 2 < col_num:
        answer = max(answer, map1[r][c] + map1[r][c + 1] + map1[r][c + 2] + map1[r + 1][c + 1])

    if r - 1 >= 0 and c + 2 < col_num:
        answer = max(answer, map1[r][c] + map1[r][c + 1] + map1[r][c + 2] + map1[r - 1][c + 1])

    if r + 2 < row_num and c + 1 < col_num:
        answer = max(answer, map1[r][c] + map1[r + 1][c] + map1[r + 2][c] + map1[r + 1][c + 1])

    if r + 2 < row_num and c - 1 >= 0:
        answer = max(answer, map1[r][c] + map1[r + 1][c] + map1[r + 2][c] + map1[r + 1][c - 1])


def type2(r, c):
    # 한쪽으로 긴 것, 주황색
    global answer
    if r + 1 < row_num and c + 2 < col_num:
        answer = max(answer, map1[r][c] + map1[r][c + 1] + map1[r][c + 2] + map1[r + 1][c])
    if r + 2 < row_num and c + 1 < col_num:
        answer = max(answer, map1[r][c] + map1[r][c + 1] + map1[r + 1][c + 1] + map1[r + 2][c + 1])

    if r + 1 < row_num and c + 2 < col_num:
        answer = max(answer, map1[r][c + 2] + map1[r + 1][c] + map1[r + 1][c + 1] + map1[r + 1][c + 2])

    if r + 2 < row_num and c + 1 < col_num:
        answer = max(answer, map1[r][c] + map1[r + 1][c] + map1[r + 2][c] + map1[r + 2][c + 1])


    if r + 1 < row_num and c + 2 < col_num:
        answer = max(answer, map1[r][c] + map1[r + 1][c] + map1[r + 1][c + 1] + map1[r + 1][c + 2])

    if r + 2 < row_num and c + 1 < col_num:
        answer = max(answer, map1[r][c] + map1[r][c + 1] + map1[r + 1][c] + map1[r + 2][c])

    if r + 1 < row_num and c + 2 < col_num:
        answer = max(answer, map1[r][c] + map1[r][c+1] + map1[r][c + 2] + map1[r + 1][c + 2])

    if r + 2 < row_num and c + 1 < col_num:
        answer = max(answer, map1[r][c+1] + map1[r+1][c + 1] + map1[r + 2][c] + map1[r + 2][c+1])

def type3(r,c):
    # 초록색
    global answer

    if r + 1 < row_num and c + 2 < col_num:
        answer = max(answer, map1[r][c + 1] + map1[r][c+2] + map1[r + 1][c ] + map1[r + 1][c + 1])

    if r + 2 < row_num and c + 1 < col_num:
        answer = max(answer, map1[r][c] + map1[r + 1][c] + map1[r + 1][c + 1] + map1[r + 2][c + 1])

    if r + 1 < row_num and c + 2 < col_num:
        answer = max(answer, map1[r][c] + map1[r][c+1] + map1[r + 1][c+1 ] + map1[r + 1][c + 2])

    if r + 2 < row_num and c + 1 < col_num:
        answer = max(answer, map1[r][c+1] + map1[r + 1][c] + map1[r + 1][c + 1] + map1[r + 2][c])


for row_index in range(row_num):
    for col_index in range(col_num):
        long1(row_index, col_index)
        square(row_index, col_index)
        type1(row_index, col_index)
        type2(row_index, col_index)
        type3(row_index, col_index)

print(answer)