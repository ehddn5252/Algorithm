def solution(rc, operations):
    row_num = len(rc)
    col_num = len(rc[0])
    # row_num 만큼 shift 하는 건 그냥 넘겨도 된다.
    # row_num * col num 만큼 rotate 하는건 그냥 넘겨도 된다.
    rc_size = row_num * col_num
    new_operations = []
    rotate_count = 0
    shift_count = 0
    now_index = 0
    for now_index in range(len(operations)):
        new_operations.append(operations[now_index])
        if operations[now_index] == "Rotate":
            rotate_count += 1
            shift_count = 0
            if rotate_count == rc_size:
                for _ in range(rotate_count):
                    new_operations.pop()
                rotate_count = 0

        else:
            shift_count += 1
            rotate_count = 0
            if shift_count == row_num:
                for _ in range(shift_count):
                    new_operations.pop()
                shift_count = 0

    for operation in new_operations:
        if operation == "Rotate":
            rotate(rc)
        else:
            shift_row(rc)
    return rc


def shift_row(rc):
    tmp = rc[-1]
    for i in range(len(rc) - 1, 0, -1):
        rc[i] = rc[i - 1]
    rc[0] = tmp


def rotate(rc):
    # 시계방향으로 rotate
    # 윗 줄을 오른쪽으로
    tmp1 = rc[0][-1]
    for i in range(len(rc[0]) - 1, 0, -1):
        rc[0][i] = rc[0][i - 1]

    # 왼줄을 위로
    for i in range(0, len(rc) - 1):
        rc[i][0] = rc[i + 1][0]

    # 아랫줄을 왼쪽으로
    for i in range(0, len(rc[0]) - 1):
        rc[-1][i] = rc[-1][i + 1]

    # 오른줄을 아래로
    for i in range(len(rc) - 1, 0, -1):
        rc[i][-1] = rc[i - 1][-1]
    rc[1][-1] = tmp1


# 효율성 9개 중 5개만 맞음.
rc1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations1 = ["Rotate", "ShiftRow"]
solution(rc1, operations1)