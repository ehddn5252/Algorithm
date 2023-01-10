from collections import deque

K = int(input())
W, H = map(int, input().split(" "))
INF = 999999999
visit = [[[False for _ in range(31)] for _ in range(201)] for _ in range(201)]
l = []
for i in range(H):
    l.append(list(map(int, input().split(" "))))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
horse_x = [-2, -1, 1, 2, 2, 1, -1, -2]
horse_y = [1, 2, 2, 1, -1, -2, -2, -1]
q = deque([(K, 0, 0, 0)])
ans = INF
while q:
    horse, x, y, times = q.popleft()
    if times >= ans:
        continue
    if x == H - 1 and y == W - 1:
        ans = times
    if horse > 0:
        for i in range(len(horse_x)):
            next_x = horse_x[i] + x
            next_y = horse_y[i] + y
            if next_x >= 0 and next_x < H and next_y >= 0 and next_y < W and not visit[next_x][next_y][horse-1]:
                if l[next_x][next_y] != 1:
                    visit[next_x][next_y][horse - 1]=True
                    q.append((horse - 1, next_x, next_y, times + 1))

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x >= 0 and next_x < H and next_y >= 0 and next_y < W and not visit[next_x][next_y][horse]:
            if l[next_x][next_y] != 1:
                visit[next_x][next_y][horse] = True
                q.append((horse, next_x, next_y, times + 1))

if ans == INF:
    print(-1)
else:
    print(ans)
