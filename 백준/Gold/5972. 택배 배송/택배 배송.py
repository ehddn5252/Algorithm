import sys
import heapq

N, M = map(int, input().split(" "))

l = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split(" "))
    l[a - 1].append((b - 1, c))
    l[b-1].append((a - 1, c))


INF = 2147000000

distance = [INF for _ in range(N)]

q = [(0, 0)]

while q:
    now_node, now_cost = heapq.heappop(q)
    for next_node, next_cost in l[now_node]:
        if distance[next_node] > now_cost + next_cost:
            distance[next_node] = now_cost + next_cost
            heapq.heappush(q, (next_node, now_cost + next_cost))
print(distance[-1])
