n, query_num = map(int, input().split(" "))
# 인덱스 1부터 시작
INF = 1000000001  # 최댓값보다 큰 수
node_relation = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split(" "))
    node_relation[a].append((b, c))
    node_relation[b].append((a, c))

from collections import deque

for _ in range(query_num):
    minimum_usado, wathcing_node = map(int, input().split(" "))
    visit = [False for _ in range(n + 1)]
    visit[wathcing_node] = True
    q = deque([[wathcing_node, INF]])
    ans = 0
    while q:
        now_node, usado = q.popleft()
        for next_node, next_usado in node_relation[now_node]:
            next_usado = min(next_usado, usado)
            if not visit[next_node] and next_usado >= minimum_usado:
                visit[next_node] = True
                ans += 1
                q.append([next_node, next_usado])
    print(ans)
