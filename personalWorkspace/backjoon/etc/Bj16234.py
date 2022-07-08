

N,L,R = map(int,input().split(" "))
l = [list(map(int,input().split(" "))) for _ in range(N)]
visit = [[0 for _ in range(N) ] for _ in range(N)]

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]
is_break = False
answer = -1
def bfs(row_index, col_index, union_num):
    global is_break
    q = []
    q.append([row_index, col_index])
    while(q):
        popped = q.pop()
        row_index = popped[0]
        col_index = popped[1]
        for i in range(4):
            next_row = row_index+d_row[i]
            next_col = col_index+d_col[i]
            if next_row >= 0 and next_row < N and next_col >= 0 and next_col < N and visit[next_row][next_col]==0:
                diff = abs(l[row_index][col_index] - l[next_row][next_col])
                if diff >= L and diff <= R:
                    # 이동이 안 일어나면 종료조건 이라서 is_break 를 여기서 False로 해준다.
                    is_break = False
                    visit[next_row][next_col] = union_num
                    q.append([next_row, next_col])


def move(union_num):
    # 연합 나라마다 평균값을 구하기 위해 sum 과 count 배열을 만든다.
    country_sum = [0 for _ in range(union_num)]
    country_count = [0 for _ in range(union_num)]
    
    # 연합 나라 체크
    for i in range(len(visit)):
        for j in range(len(visit[0])):
            country_sum[visit[i][j]]+=l[i][j]
            country_count[visit[i][j]]+=1

    country_result = [0 for _ in range(union_num)]
    # 연합 나라별 평균값 구해준다.
    for i in range(1,len(country_count)):
        country_result[i] = int(country_sum[i]/country_count[i])
    
    # 나라별 인구 재설정
    for i in range(len(visit)):
        for j in range(len(visit[0])):
            l[i][j] = country_result[visit[i][j]]


def reset_visit():
    global visit
    # visit 초기화
    visit = [[0 for _ in range(N)] for _ in range(N)]

while not is_break:
    is_break = True
    union_num = 1
    for row_index, row in enumerate(l):
        for col_index, col in enumerate(row):
            if visit[row_index][col_index]==0:
                visit[row_index][col_index] = union_num
                bfs(row_index,col_index,union_num)
                union_num+=1

    move(union_num)
    reset_visit()
    answer+=1
print(answer)