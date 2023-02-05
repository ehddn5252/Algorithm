# 부메랑 모양 1 (0,0) (0,1) (1,1)  // 2 (1,0),(0,1),(1,1)
#  3 (0,0) (1,0), (1,1) // 4 (0,0) (1,0) (0,1)

def check_v(i, j, version_flag, now_score):
    ans = 0

    if version_flag == "v1":
        if i + 1 < N and j - 1 >= 0:
            if not visit[i][j - 1] and not visit[i][j] and not visit[i + 1][j]:
                visit_check(i, j, version_flag, True)
                ans = l[i][j - 1] + (2 * l[i][j]) + l[i + 1][j]
                dfs(i, j + 1, now_score + ans)
                visit_check(i, j, version_flag, False)
    elif version_flag == "v2":
        if i - 1 >= 0 and j - 1 >= 0:
            if not visit[i - 1][j] and not visit[i][j] and not visit[i][j - 1]:
                visit_check(i, j, version_flag, True)
                ans = l[i - 1][j] + 2 * l[i][j] + l[i][j - 1]
                dfs(i, j + 1, now_score + ans)
                visit_check(i, j, version_flag, False)


    elif version_flag == "v3":
        if i - 1 >= 0 and j + 1 < M:
            if not visit[i - 1][j] and not visit[i][j] and not visit[i][j + 1]:
                visit_check(i, j, version_flag, True)
                ans = l[i - 1][j] + (2 * l[i][j]) + l[i][j + 1]
                dfs(i, j + 1, now_score + ans)
                visit_check(i, j, version_flag, False)


    elif version_flag == "v4":
        if i + 1 < N and j + 1 < M:
            if not visit[i][j] and not visit[i][j + 1] and not visit[i + 1][j]:
                visit_check(i, j, version_flag, True)
                ans = (2 * l[i][j]) + l[i][j + 1] + l[i + 1][j]
                dfs(i, j + 1, now_score + ans)
                visit_check(i, j, version_flag, False)

def visit_check(i, j, version, action_flag):
    global visit
    if version == "v1":
        visit[i][j - 1] = action_flag
        visit[i][j] = action_flag
        visit[i + 1][j] = action_flag

    elif version == "v2":
        visit[i - 1][j] = action_flag
        visit[i][j] = action_flag
        visit[i][j - 1] = action_flag
    elif version == "v3":
        visit[i - 1][j] = action_flag
        visit[i][j] = action_flag
        visit[i][j + 1] = action_flag
    elif version == "v4":
        visit[i][j] = action_flag
        visit[i][j + 1] = action_flag
        visit[i + 1][j] = action_flag


def dfs(input_i, input_j, now_score):
    global max_value
    if input_j == M:
        input_i += 1
        input_j = 0
    if input_i == N:
        max_value = max(max_value, now_score)
        return
    if not visit[input_i][input_j]:
        for version in versions:
            check_v(input_i, input_j, version, now_score)
    dfs(input_i, input_j + 1, now_score)


N, M = map(int, input().split(" "))
l = []
visit = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    l.append(list(map(int, input().split(" "))))

max_value = 0
versions = ["v1", "v2", "v3", "v4"]
dfs(0, 0, 0)

print(max_value)
