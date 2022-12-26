from collections import deque

num = int(input())
l = []
for i in range(num):
    l.append(list(map(int, input().split(" "))))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j,n):
    q = deque([(i, j)])
    while q:
        popped_i, popped_j = q.popleft()

        for i in range(4):
            next_i = dx[i] + popped_i
            next_j = dy[i] + popped_j

            if next_i < num and next_j < num and next_i >= 0 and next_j >= 0 and l[next_i][next_j] > n and not \
            visit[next_i][next_j]:
                visit[next_i][next_j] = True
                q.append((next_i, next_j))


max_ans = 0
for n in range(0, 101):
    ans = 0
    visit = [[False for i in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if not visit[i][j] and l[i][j] > n:
                visit[i][j] = True
                ans += 1
                bfs(i, j,n)

    if ans > max_ans:
        max_ans = ans

print(max_ans)
