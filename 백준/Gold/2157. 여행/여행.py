N, M, K = map(int, input().split(" "))
# 도시번호가 증가하는 순서로만 이동
l = [[] for _ in range(N)]

from collections import deque

q = deque([(0, 1, 0)])

for _ in range(K):
    a, b, c = map(int, input().split(" "))
    if a > b: continue
    l[a - 1].append([b - 1, c])

visit_max = [[0, 0] for _ in range(N)]
ans = 0
# 일단 완탐 갈겨보자.
while q:
    now_node, visit_times, now_value = q.popleft()
    if visit_times > M:
        continue
    if now_node == N - 1 and visit_times <= M:
        if ans < now_value:
            ans = now_value
            continue

    for next_node in l[now_node]:
        if visit_max[next_node[0]][0] >= now_value + next_node[1] and visit_max[next_node[0]][1] <= visit_times + 1:
            continue
        else:
            visit_max[next_node[0]] = [now_value + next_node[1], visit_times + 1]
            q.append((next_node[0], visit_times + 1, now_value + next_node[1]))
print(ans)
