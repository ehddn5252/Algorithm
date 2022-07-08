# 연구소 3

# 맨 처음에는 모든 칸이 비활성 상태이고 이 중 몇개만 활성상태로 바꿔서 연구소 전체에 퍼뜨리는 최소 시간을 구해야 한다.
# 풀이 방법
# 1. 각 좌표들을 list 에 넣는다.
# 2. 그것들의 조합으로 m 개를 고른다.
# 3. 이것으로 BFS 돌린다. 벽인 경우에는 맨 처음에 -1 로 표시해줘야 한다.
# 4. 빈 공간은 0 벽은 1, 바이러스는 2이다.
# (비활성화 바이러스도 바이러스로 취급된다. 참고하자)


from itertools import combinations
from collections import deque

map_size,active_virus_num = map(int,input().split(" "))
map1 = [list(map(int, input().split(" "))) for _ in range(map_size)]
ans = 9999999
l = []
check_0 = False
saved_zero_count = 0

# 비활성 바이러스를 -3 표시, 벽은 -2 표시 활성 바이러스는 -1로 빈 칸은 0 표시
for row_index, row in enumerate(map1):
    for col_index, col in enumerate(row):
        if(map1[row_index][col_index]==2):
            l.append([row_index, col_index])
            map1[row_index][col_index] = -3
        elif(map1[row_index][col_index]==1):
            map1[row_index][col_index]=-2
        if(map1[row_index][col_index]==0):
            saved_zero_count+=1
            check_0=True

import copy
d = [[0,1],[0,-1],[-1,0],[1,0]]
break_flag=False
if check_0:
    can_complete = False
    for active_viruses in combinations(l,active_virus_num):
        zero_count=saved_zero_count
        use_map = copy.deepcopy(map1)
        q = deque([])
        for active_virus_row, active_virus_col in active_viruses:
            q.append([active_virus_row,active_virus_col,0])
            # 활성 바이러스 표시
            use_map[active_virus_row][active_virus_col] = -1

        ans_candidate = 0
        while q and zero_count>0:
            popped = q.pop()
            for i in range(4):
                next_r=d[i][0] + popped[0]
                next_c=d[i][1] + popped[1]
                # 비활성인 바이러스만 남았을 때 안 퍼지게 하는 방법은 무엇인가?
                if(next_r>=0 and next_r<len(map1) and next_c>=0 and next_c<len(map1[0])):
                    if use_map[next_r][next_c] == 0 or use_map[next_r][next_c]==-3:
                        if(use_map[next_r][next_c] == 0):
                            zero_count-=1
                        use_map[next_r][next_c] = popped[2]+1
                        q.appendleft([next_r, next_c, popped[2]+1])
                        if(ans_candidate < popped[2]+1):
                            ans_candidate = popped[2]+1

                        if zero_count==0:
                            break

        break_flag = False
        for row_index, row in enumerate(use_map):
            for col_index, col in enumerate(row):
                if(col==0):
                    break_flag = True
                    break
            if(break_flag):
                break
        if not break_flag:
            can_complete = True
            if ans_candidate < ans:
                ans = ans_candidate
    if not can_complete:
        ans=-1
    print(ans)
else:
    print(0)