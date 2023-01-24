from collections import deque
import math, sys

N, M, K = map(int, sys.stdin.readline().split(" "))
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
robot_map = []
for _ in range(N):
    robot_map.append(list(map(int, sys.stdin.readline().split(" "))))

food_map = [[5 for _ in range(N)] for _ in range(N)]
tree_q = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    tmp_l = list(map(int, sys.stdin.readline().split(" ")))
    tree_q[tmp_l[0] - 1][tmp_l[1] - 1].append(tmp_l[2])

for i in range(N):
    for j in range(N):
        tmp = tree_q[i][j]
        tmp = sorted(list(tmp))
        tree_q[i][j] = deque(tmp)
time = 0
ans = 0
next_tree_q = deque([])
die_tree_q = []

for year in range(K):
    # spring
    for i in range(N):
        for j in range(N):
            start = 0
            end = len(tree_q[i][j])
            while start < end:
                start += 1
                k = tree_q[i][j].popleft()
                if k > food_map[i][j]:
                    die_tree_q.append((i, j, k))
                else:
                    food_map[i][j]-=k
                    tree_q[i][j].append(k + 1)

    # in summer
    for i in range(len(die_tree_q)):
        now_i, now_j, age = die_tree_q[i]
        food_map[now_i][now_j] += math.trunc(age/2)
    die_tree_q.clear()
    # in fall
    for i in range(N):
        for j in range(N):
            end = len(tree_q[i][j])
            for k in range(end):
                if tree_q[i][j][k] % 5 == 0:
                    for tt in range(8):
                        next_i = i + dx[tt]
                        next_j = j + dy[tt]
                        if next_i >= 0 and next_i < N and next_j >= 0 and next_j < N:
                            tree_q[next_i][next_j].appendleft(1)

    for i in range(N):
        for j in range(N):
            food_map[i][j] += robot_map[i][j]

for i in range(N):
    for j in range(N):
        ans += len(tree_q[i][j])
print(ans)
