from collections import deque

F, S, G, U, D = map(int, input().split(" "))  # F: 총 높이 G: 목표지점, S: 시작지점, U: 위로 이동 D: 아래로 이동
CANT: str = "use the stairs"
l = []
INF = 99999999
ans = INF
q = deque([(S, 0)])
visit = [False for i in range(F + 1)]
visit[S]=True
while q:
    now, now_click = q.popleft()
    if now == G:
        ans = min(ans, now_click)
    next1 = now + U
    next2 = now - D

    if next1 <= F and next1 >= 1 and not visit[next1]:
        visit[next1] = True
        q.append((next1, now_click + 1))
    if next2 <= F and next2 >= 1 and not visit[next2]:
        visit[next2] = True
        q.append((next2, now_click + 1))

if ans == INF:
    print(CANT)
else:
    print(ans)
