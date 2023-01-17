h, w = map(int, input().split(" "))

l = []

for _ in range(h):
    l.append(list(map(int, input().split(" "))))

from collections import deque

visit = [[False for _ in range(w)] for _ in range(h)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
q = deque([(0, 0)])
next_q = deque([])
ans = 0
time = 0
from copy import deepcopy
visit[0][0]=True
while True:
    while q:
        now_i, now_j = q.popleft()
        for i in range(4):
            next_i = di[i] + now_i
            next_j = dj[i] + now_j
            if next_i >= 0 and next_i < h and next_j >= 0 and next_j < w:
                if not visit[next_i][next_j]:
                    visit[next_i][next_j] = True
                    if l[next_i][next_j] == 1:
                        next_q.append((next_i, next_j))
                    else:
                        q.append((next_i, next_j))
    if len(next_q) == 0:
        break
    time += 1
    ans = len(next_q)
    q = deepcopy(next_q)
    next_q.clear()
print(time)
print(ans)
