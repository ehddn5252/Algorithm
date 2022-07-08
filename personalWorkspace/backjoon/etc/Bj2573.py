from pprint import pprint

row_num, col_num = map(int,input().split(" "))

ice_map = [list(map(int, input().split(" ")))for _ in range(row_num)]
visit_map = [[0 for _ in range(col_num)] for _ in range(row_num)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
all_melt_flag = True
year = 0

def BFS(row_index, col_index, split_index):
    global visit_map
    q = [[row_index,col_index]]

    while q:
        popped = q.pop()
        for i in range(4):
            next_row = popped[0] + dr[i]
            next_col = popped[1] + dc[i]
            if next_row >= 0 and next_row < row_num and next_col >= 0 and next_col < col_num and visit_map[next_row][next_col]==0:
                if ice_map[next_row][next_col]!=0:
                    visit_map[next_row][next_col] = split_index
                    q.append([next_row, next_col])



def melt():
    global all_melt_flag, visit_map
    for i in range(1, row_num-1):
        for j in range(1, col_num-1):
            if ice_map[i][j]!=0:
                all_melt_flag = False
                zero_count = 0
                for k in range(4):
                    next_row = i + dr[k]
                    next_col = j + dc[k]
                    if next_row >= 0 and next_row < row_num and next_col >= 0 and next_col < col_num:
                        if ice_map[next_row][next_col]==0 and visit_map[next_row][next_col]==0:
                            zero_count+=1
                ice_map[i][j]-=zero_count
                if ice_map[i][j]<0:
                    ice_map[i][j]=0

def reset_variable():
    global visit_map, all_melt_flag
    visit_map = [[0 for _ in range(col_num)] for _ in range(row_num)]
    all_melt_flag = True

while True:
    split_index = 1
    for i in range(1, row_num-1):
        for j in range(1, col_num-1):
            if ice_map[i][j]!=0 and visit_map[i][j]==0:
                BFS(i, j, split_index)
                split_index += 1

    if split_index >= 3:
        print(year)
        break

    melt()
    if all_melt_flag==True:
        print(0)
        break
    year += 1
    reset_variable()

