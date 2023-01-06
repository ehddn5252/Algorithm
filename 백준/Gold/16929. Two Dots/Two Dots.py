N, M = map(int, input().split(" "))

l = []
for i in range(N):
    l.append(input())

visit = [[0 for i in range(M)] for _ in range(N)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


def dfs(input_i, input_j, level, start_i, start_j):
    global ans
    if ans == "Yes":
        return
    for i in range(4):
        next_i = input_i + di[i]
        next_j = input_j + dj[i]
        if next_i >= 0 and next_i < N and next_j >= 0 and next_j < M:
            if next_i == start_i and next_j == start_j and level > 1 and l[input_i][input_j] == l[next_i][next_j]:
                ans = "Yes"
                return

            if visit[next_i][next_j] == 0 and l[input_i][input_j] == l[next_i][next_j]:
                visit[next_i][next_j] = 1
                dfs(next_i, next_j, level + 1, start_i, start_j)
                visit[next_i][next_j] = 0

ans = "No"

for i in range(N):
    for j in range(M):
        if ans == "Yes":
            break
        if visit[i][j] == 0:
            visit[i][j] = 2  # start
            dfs(i, j, 0, i, j)
print(ans)
