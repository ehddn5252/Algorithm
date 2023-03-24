import heapq

N, M, X = map(int, input().split(" "))  # 학생수, M줄 수, X의 집에 오는 데 가장 오래 걸리는 학생의 소요시간
INF = 2147483647
l = [[] for _ in range(N + 1)]
visit = [INF for _ in range(N + 1)]
visit[0] = 0
l2 = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split(" "))
    l[a].append([t, b])
    l2[b].append([t, a])


def dijkstra(start_node, node_list, input_visit):
    q = []
    start = (0, start_node)
    input_visit[start_node] = 0
    heapq.heappush(q, start)
    while q:
        cost_time, node = q.pop()
        for time, to_node in node_list[node]:
            if input_visit[to_node] > time + cost_time:
                input_visit[to_node] = time + cost_time
                heapq.heappush(q, (time + cost_time, to_node))
    return input_visit


import copy

v1 = dijkstra(X, l, copy.deepcopy(visit))
v2 = dijkstra(X, l2, copy.deepcopy(visit))
max_value = 0
for i in range(len(v1)):
    if v1[i] + v2[i] > max_value:
        max_value = v1[i] + v2[i]
print(max_value)
