# 진우의 달 여행

N, M = map(int, input().split(" "))

dp = []
for _ in range(N):
    tmp = list(map(int, input().split(" ")))
    dp.append(tmp)

"""
dp로 해결할 수 있다,
1. 맨 위에서부터 시작한다.
2. 왼쪽 아래, 바로 아래, 오른쪽 아래 3곳 중 가장 값이 큰 값을 확인하고 현재 위치에 값을 더한다.
dp[i][j]= dp[i][j]+max(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
before flag 를 살펴봐야한다.
근데 전에 움직인 방향으로 움직이면 안된다. 
생각하기가 어렵다.
-> 그렇다면 답은 DFS
1. 시작 위치를 넣는 다.
2. 다음 위치를 넣는 데, 이전에 움직인 flag와 같이 움직이면 안된다.

"""

dx = [0, -1, 1]


def dfs(cnt, now_position, before):
    if cnt == N:
        return 0
    ret = INF

    for i in range(3):
        if before == i: continue
        if now_position + dx[i] < 0 or now_position + dx[i] >= M: continue
        ret = min(ret, dfs(cnt + 1, now_position + dx[i], i)+dp[cnt][now_position])
    return ret


INF = 2147483647
ans = INF
for i in range(M):
    ans = min(dfs(0, i, -1), ans)

print(ans)
