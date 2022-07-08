import heapq
V, E = map(int,input().split(" "))

start_node = int(input())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split(" "))
    adj[s].append([w, e])

INF = 20000 * 10 + 1
distance = [INF for _ in range(V+1)]
distance[start_node] = 0
hq = []
heapq.heappush(hq, [0, start_node])
while hq:
    popped_weight, popped_vertex = heapq.heappop(hq)

    for current_w, current_v in adj[popped_vertex]:
        if popped_weight + current_w < distance[current_v]:
            distance[current_v] = popped_weight + current_w
            heapq.heappush(hq, [distance[current_v], current_v])

for i, v in enumerate(distance):
    if i == 0:continue
    if v != INF:print(v)
    else:print("INF")




