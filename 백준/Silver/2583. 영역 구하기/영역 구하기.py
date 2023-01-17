import sys
sys.setrecursionlimit(100000)

R, C, K = map(int, input().split(" "))
l = []
for i in range(R):
    l.append([0 for _ in range(C)])

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split(" "))
    for i in range(y1,y2):
        for j in range(x1, x2):
            l[i][j] = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visit = [[False for i in range(C)] for _ in range(R)]


def dfs(now_i, now_j):
    global width
    for i in range(4):
        next_i = now_i + dx[i]
        next_j = now_j + dy[i]

        if next_i >= 0 and next_i < R and next_j >= 0 and next_j < C:
            if not visit[next_i][next_j] and l[next_i][next_j] == 0:
                visit[next_i][next_j] = True
                width += 1
                dfs(next_i, next_j)


start_num = 2
ans_list = []
for i in range(R):
    for j in range(C):
        if not visit[i][j] and l[i][j]==0:
            start_num += 1
            width = 1
            visit[i][j] = True
            dfs(i, j)
            ans_list.append(width)

ans_list.sort()

print(start_num - 2)
print(" ".join( str(i) for i in ans_list))