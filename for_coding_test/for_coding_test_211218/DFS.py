# 벽부수고 이동하기

# 문제 요약
# 1. N x M 행룔로 표현되는 맵이 있다. 
# 2. 0 은 이동할 수 있는 곳을 나타내고 1은 이동할 수 없는 곳을 나타낸다.
# 3. 당신은 1,1에서 N,M의 위치까지 이동하려 한다.
# 4. 당신은 (1,1)에서 (N,M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
# 5. 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면 벽을 
# 6. 벽을 한 개까지 부수고 이동해도 된다.
#  

# 해결 방법
"""

파이썬은 1 초당 2000만번의 연산을 할 수 있다
맵의 크기가 이 경우 1000 * 1000 =100만 이다.
정리.
1. 움직일 때는 일단 주변에 0이 있으면 그것을 기점으로 DFS를 사용한다.
2. DFS 를 사용할 때, 오른쪽이나 아래에 1이 있다면 그것을 부수는 경우를 만들고 다시 안부수는 것을 세팅
3. 만약
"""
import sys
sys.setrecursionlimit(1000000)
# input
row_num, col_num = map(int,sys.stdin.readline().split())
d_col = [-1,1,0,0]
d_row = [0,0,-1,1]
i=0
answer=9999999999
def backtracking(row,col,maze_map, break_flag:bool, visit_map, day):
    global answer

    if day>answer:
        return
    if  row<0 or row>=row_num or col<0 or col>=col_num:
        return
    if row==row_num-1 and col == col_num-1:
        if day <= answer:
            answer=day

    for i in range(4):
        now_row = row + d_row[i]
        now_col = col + d_col[i]
        if 0 <= now_row and now_row<row_num and 0 <= now_col and now_col < col_num:
            if maze_map[now_row][now_col]=="1" and break_flag==False and visit_map[now_row][now_col]==False:
                break_flag=True
                visit_map[now_row][now_col]=True
                maze_map[now_row][now_col]=1
                backtracking(now_row, now_col, maze_map, break_flag, visit_map, day+1)
                break_flag=False
                visit_map[now_row][now_col]=False
                maze_map[now_row][now_col]=0

            elif maze_map[now_row][now_col]=="0" and visit_map[now_row][now_col]==False:
                visit_map[now_row][now_col]=True
                maze_map[now_row][now_col]=1
                backtracking(now_row, now_col,maze_map, break_flag, visit_map, day+1)
                maze_map[now_row][now_col]=0
                visit_map[now_row][now_col]=False


if __name__=="__main__":
    maze_map: list = [[i for i in input()] for _ in range(row_num)]
    visit_map = [[False for _ in range(col_num)] for _ in range(row_num) ]
    backtracking(row=0, col=0, break_flag=False, maze_map=maze_map, visit_map=visit_map, day=1)

    if answer!=9999999999:
        print(answer)
    else:
        print(-1)
