R, C, K = map(int, input().split(" "))
l = []
for i in range(R):
    l.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[False for _ in range(C)] for _ in range(R)]

ans = 0

def dfs(now_i,now_j,now_distance):
    global ans
    if now_i == 0 and now_j == C - 1 and K==now_distance and l[now_i][now_j]!='T':
        ans += 1
        return
    for i in range(4):
        next_i = now_i+dx[i]
        next_j = now_j+dy[i]
        if next_i >= 0 and next_i < R and next_j >= 0 and next_j < C:
            if l[next_i][next_j] == '.' and not visit[next_i][next_j]:
                visit[next_i][next_j]=True
                dfs(next_i, next_j, now_distance + 1)
                visit[next_i][next_j]=False

visit[R-1][0]=True
dfs(R - 1, 0, 1)
print(ans)