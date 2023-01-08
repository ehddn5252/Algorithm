import heapq

N = int(input())
r1, c1, r2, c2 = map(int, input().split(" "))

d = [(-2, -1), (-2, 1), (0, -2), (0, +2), (2, -1), (2, 1)]

q = [(0, r1, c1)]
visit = [[0 for i in range(N)] for _ in range(N)]
visit[r1][c1] = 1
ans = -1
while q:
    popped = heapq.heappop(q)
    if popped[1] == r2 and popped[2] == c2:
        ans = popped[0]
    for i in range(6):
        now_r = popped[1] + d[i][0]
        now_c = popped[2] + d[i][1]

        if now_r < N and now_r >= 0 and now_c < N and now_c >= 0:
            if visit[now_r][now_c] > popped[0] + 1 or visit[now_r][now_c] == 0:
                visit[now_r][now_c] = popped[0] + 1
                heapq.heappush(q, (popped[0] + 1, now_r, now_c))

print(ans)
