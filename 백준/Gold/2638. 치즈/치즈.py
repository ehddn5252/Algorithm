import copy

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

R, C = map(int, input().split(" "))

l = []
visit = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(R):
    l.append(list(map(int, input().split(" "))))

from collections import deque

q = deque([(0, 0)])
next_q = deque([])
# 바깥 공기 도는 q
out_q = deque([(0, 0)])
time = 0

visit[0][0] = True
import copy

while True:
    while out_q:
        now_i, now_j = out_q.popleft()
        for i in range(4):
            next_i = now_i + di[i]
            next_j = now_j + dj[i]
            if next_i >= 0 and next_i < R and next_j >= 0 and next_j < C:
                if visit[next_i][next_j] == 0 and l[next_i][next_j] == 0:
                    visit[next_i][next_j] = -1

    while q:
        now_i, now_j = q.popleft()
        for i in range(4):
            next_i = now_i + di[i]
            next_j = now_j + dj[i]
            if next_i >= 0 and next_i < R and next_j >= 0 and next_j < C:
                if visit[next_i][next_j] == -1 or visit[next_i][next_j] == 0:
                    if l[next_i][next_j] == 1:
                        count = 0
                        for j in range(4):
                            next_next_i = next_i + di[j]
                            next_next_j = next_j + dj[j]
                            if next_next_i >= 0 and next_next_i < R and next_next_j >= 0 and next_next_j < C:
                                if l[next_next_i][next_next_j] == 0 and visit[next_next_i][next_next_j] != 0:
                                    count += 1
                            if count >= 2:
                                break
                        if count >= 2:
                            visit[next_i][next_j] = 1
                            next_q.append((next_i, next_j))
                    else:
                        visit[next_i][next_j] = 1
                        q.append((next_i, next_j))
    if len(next_q) == 0:
        break
    else:
        q = copy.deepcopy(next_q)
        out_q = copy.deepcopy(next_q)
        while next_q:
            i, j = next_q.popleft()
            l[i][j] = 0
        time += 1

print(time)
