# input
N, M, K = map(int, input().split(" "))
l = []
dp = [[[-1 for i in range(81)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    l.append(list(map(str, input())))

word = input()
ans = 0

d = []
for i in range(1, K + 1):
    d.append((i, 0))
    d.append((-i, 0))
    d.append((0, i))
    d.append((0, -i))


def dfs(start_i, start_j, cnt):
    global ans, word
    if dp[start_i][start_j][cnt] != -1:
        return dp[start_i][start_j][cnt]
    if cnt == len(word):
        return 1
    dp[start_i][start_j][cnt] = 0
    for i in range(len(d)):
        next_i = d[i][0] + start_i
        next_j = d[i][1] + start_j
        if next_i >= 0 and next_i < N and next_j >= 0 and next_j < M:
            if word[cnt] == l[next_i][next_j]:
                dp[start_i][start_j][cnt] += dfs(next_i, next_j, cnt + 1)

    return dp[start_i][start_j][cnt]


# 최대 K칸까지 이동
for i in range(N):
    for j in range(M):
        if l[i][j] == word[0]:
            ans+=dfs(i, j, 1)

print(ans)
