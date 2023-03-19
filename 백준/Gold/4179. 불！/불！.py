# #은 벽, .은 통로, J는 지훈, F 는 불의 위치

# 불은 4방향 확산, 지훈이는 1초에 한 칸씩 이동
# 지훈이부터 이동시키고 불 이동시키기
from collections import deque
import copy

R, C = map(int, input().split(" "))
l = [[] for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
fires = deque([])
next_fires = deque([])
jihun_q = deque([])
visit = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    tmp_input = input()
    for j in range(C):
        append_val = tmp_input[j]
        if append_val == 'J':
            jihun_q.append((i, j))
            append_val = '.'
        elif append_val == 'F':
            fires.append((i, j))
        l[i].append(append_val)


def is_not_out_of_range(next_i, next_j):
    if next_i >= 0 and next_i < R and next_j >= 0 and next_j < C:
        return True
    else:
        return False


def is_answer_condition(now_i, now_j):
    if now_i == 0 or now_i == R - 1 or now_j == 0 or now_j == C - 1:
        return True
    else:
        return False


nextq = deque([])
time = 1
answer_flag = False
while True:
    while jihun_q:
        now_i, now_j = jihun_q.popleft()
        if l[now_i][now_j] == 'F':
            continue
        if is_answer_condition(now_i, now_j):
            answer_flag = True
            break

        for i in range(4):
            next_i = dy[i] + now_i
            next_j = dx[i] + now_j
            if is_not_out_of_range(next_i, next_j):
                next_time = time + 1
                if (visit[next_i][next_j] == 0 or visit[next_i][next_j] > next_time) and l[next_i][next_j] == '.':
                    visit[next_i][next_j] = next_time
                    nextq.append((next_i, next_j))

    jihun_q = copy.deepcopy(nextq)
    if answer_flag or not nextq:
        break
    nextq.clear()

    while fires:
        now_i, now_j = fires.popleft()
        for i in range(4):
            next_i = dy[i] + now_i
            next_j = dx[i] + now_j
            if is_not_out_of_range(next_i, next_j):
                if l[next_i][next_j] == '.':
                    l[next_i][next_j] = 'F'
                    next_fires.append((next_i, next_j))

    fires = copy.deepcopy(next_fires)
    next_fires.clear()
    time += 1
if not answer_flag:
    print("IMPOSSIBLE")
else:
    print(time)
