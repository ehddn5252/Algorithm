import sys
from collections import deque
col_num, row_num = map(int,sys.stdin.readline().split())

box_map = []
for i in range(row_num):
    box_map.append(sys.stdin.readline().split())

d_col = [-1, 1, 0, 0]
d_row = [0, 0, -1, 1]
max_date:int=0
queue:list=deque()
not_all_riped:bool=False


for row in range(row_num):
    for col in range(col_num):
        if not not_all_riped and box_map[row][col]=='0':
            not_all_riped=True
        if box_map[row][col]=='1':
            queue.append((row,col,0))

if not_all_riped:
    while queue:
        popped_row, popped_col, passed_date = queue.popleft()
        if max_date<passed_date:
            max_date=passed_date
        for i in range(4):
            #four_direction_not_0=False
            now_row = d_row[i]+popped_row
            now_col = d_col[i]+popped_col
            if now_col>=0 and now_col< col_num and now_row >=0 and now_row < row_num:
                if box_map[now_row][now_col]=='0':
                    box_map[now_row][now_col]='1'
                    queue.append((now_row, now_col, passed_date+1))

    cant_riped=False
    for row in range(row_num):
        for col in range(col_num):
            if box_map[row][col]=='0':
                cant_riped=True
                break
        if cant_riped:
            break

    if cant_riped:
        print(-1)
    else:
        print(max_date)
else:
    print(0)
