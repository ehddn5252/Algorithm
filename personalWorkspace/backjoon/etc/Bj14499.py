# 주사위 굴리기
import sys

N, M, y, x, K = map(int, input().split(" "))
map1 = []
dice = [0, 0, 0, 0, 0, 0]

# 동 서 북 남
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]


def dice_move(num):
    global x, y
    # 동 서 북 남 1,2,3,4
    if num == 1:
        tmp = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[3]
        dice[3] = tmp

    elif num == 2:
        tmp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[3]
        dice[3] = dice[5]
        dice[5] = tmp


    elif num == 3:
        tmp = dice[3]
        dice[3] = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[0]
        dice[0] = tmp

    elif num == 4:
        tmp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[3]
        dice[3] = tmp

    if map1[y][x] != 0:
        dice[1] = map1[y][x]
        map1[y][x] = 0
    else:
        map1[y][x] = dice[1]
    print(dice[3])


for i in range(N):
    map1.append(list(map(int, sys.stdin.readline().split(" "))))

commands = list(map(int, sys.stdin.readline().split(" ")))
index = 0
while index < len(commands):
    new_x = x + dx[commands[index]]
    new_y = y + dy[commands[index]]
    if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N:
        x = new_x
        y = new_y
        dice_move(commands[index])
    index += 1
