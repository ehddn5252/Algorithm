n = int(input())
l = []

# 상어 자리는 9, N 최대 20, 아기 상어 첫 크기는 2

class node:
    def __init__(self, time, i, j):
        self.time = time
        self.i = i
        self.j = j

    def __lt__(self, other):
        if self.time < other.time:
            return True
        elif self.time == other.time:
            if self.i != other.i:
                return self.i < other.i
            else:
                return self.j < other.j


from collections import deque

fish = [0, 0, 0, 0, 0, 0, 0]
q = []
for i in range(n):
    tmp_l = list(map(int, input().split(" ")))
    for j in range(len(tmp_l)):
        if tmp_l[j] != 0:
            q.append((tmp_l[j], i, j))
        if tmp_l[j]!=9:
            fish[tmp_l[j]] += 1
    l.append(tmp_l)

q.sort(key=lambda x: (x[0], x[1], x[2]))

_, shark_i, shark_j = q.pop()
l[shark_i][shark_j] = 0
q = deque(q)
shark_size = 2

inner_q = [node(0, shark_i, shark_j)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
total_time = 0
eat = 0

import heapq

times = 0
while q:
    times += 1
    # fish_size, now_destination_i, now_destination_j = q.popleft()
    q.popleft()
    visit = [[0 for _ in range(n)] for _ in range(n)]
    is_can_go_size = 0
    for i in range(1,len(fish)):
        if i < shark_size:
            is_can_go_size += fish[i]
    if is_can_go_size == 0:
        break
    while inner_q:
        node1 = heapq.heappop(inner_q)
        move_time, now_i, now_j = node1.time, node1.i, node1.j
        if l[now_i][now_j] != 0 and l[now_i][now_j] < shark_size:
            fish[l[now_i][now_j]] -= 1
            eat += 1
            if eat == shark_size:
                shark_size = shark_size + 1
                eat = 0
            total_time += move_time
            l[now_i][now_j] = 0
            inner_q.clear()
            heapq.heappush(inner_q, node(0, now_i, now_j))
            break
        for i in range(4):
            next_i = now_i + dx[i]
            next_j = now_j + dy[i]
            if next_i >= 0 and next_i < n and next_j >= 0 and next_j < n:
                if (visit[next_i][next_j] == 0 or visit[next_i][next_j] > move_time + 1) and l[next_i][
                    next_j] <= shark_size:
                    visit[next_i][next_j] = move_time + 1
                    heapq.heappush(inner_q, node(move_time + 1, next_i, next_j))

print(total_time)
