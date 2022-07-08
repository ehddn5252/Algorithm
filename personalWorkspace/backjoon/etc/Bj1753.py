import heapq

# 정점과 간선
V, E = map(int,input().split(" "))
# 시작 노드
start_node = int(input())
# 인접 행렬
adj = [[] for i in range(V+1)]

for i in range(E):
    s, e, w = map(int, input().split(" "))
    adj[s].append([w, e])

INF = 1000000000
hq = []
# 거리가 저장된 배열
distance = [INF for i in range(V+1)]
# 시작 노드 거리 초기화
distance[start_node]=0

heapq.heappush(hq,[0,start_node])
while hq:
    current_w, current_node = heapq.heappop(hq)

    # if dist[current_node] != current_w: continue

    for nw,nv in adj[current_node]:
        # 현재까지 온 가중치 + 지금 노드사이의 가중치
        if current_w + nw <distance[nv]:
            distance[nv] = current_w + nw
            heapq.heappush(hq,[distance[nv],nv])
    #
    # for j in range(V):
    #     if distance[current_node] + adj[current_node][j][0] < distance[j]:
    #         distance[j] = distance[current_node] + adj[current_node][j][0]
    #         heapq.heappush(hq,[distance[j],j])

for i,v in enumerate(distance):
    if i==0: continue
    if v!=INF: print(v)
    else: print("INF")
