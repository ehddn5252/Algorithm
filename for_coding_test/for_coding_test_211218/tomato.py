# M, N, H: 상자의 col, 상자의 row, 상자의 hight

from collections import deque

# input
col_num, row_num, hight_num=map(int, input().split())

# box setting
box: list = [[] for i in range(hight_num)]
for hight_index in range(hight_num):
    for row in range(row_num):
        box[hight_index].append(list(map(int,input().split())))


d_col = [-1, 1, 0, 0, 0, 0]
d_row = [0, 0, -1, 1, 0, 0]
d_h = [0, 0, 0, 0, -1, 1]

answer:int = 0
day:int = 0
all_riped: bool=True
break_flag=False

for hight_index in range(hight_num):
    for row_index in range(row_num):
        for col_index in range(col_num):
            if box[hight_index][row_index][col_index]==0:
                all_riped=False
                break_flag=True
                break
        if break_flag:
            break
    if break_flag:
        break


if not all_riped:
    queue:deque = deque([])
    for hight_index in range(hight_num):
        for row_index in range(row_num):
            for col_index in range(col_num):
                if box[hight_index][row_index][col_index]==1:
                    queue.append([hight_index, row_index, col_index, 0])
    
    while queue:
        location_info_list=queue.popleft()
        for i in range(6):
            h = d_col[i] + location_info_list[0]
            row = d_row[i] + location_info_list[1]
            col = d_h[i] + location_info_list[2]
            if location_info_list[3]>day:
                day = location_info_list[3]
            if 0 <= col and col < col_num and 0 <= row and row < row_num and 0 <= h and h < hight_num:
                if box[h][row][col] == 0:
                    box[h][row][col] = 1
                    queue.append([h,row,col,location_info_list[3]+1])

    answer=day

    break_flag = False
    for hight_index in range(hight_num):
        for row_index in range(row_num):
            for col_index in range(col_num):
                if box[hight_index][row_index][col_index]==0:
                    answer = -1
                    break_flag=True
                    break
            if break_flag:
                break
        if break_flag:
            break

else:
    answer=0

print(answer)