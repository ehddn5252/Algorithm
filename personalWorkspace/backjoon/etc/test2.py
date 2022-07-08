import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize
# 정정과 간선
V, E = map(int, input().split())
# 시작 노드
K = int(input())

# 인접 행렬
edge = [[] for _ in range(V+1)]
# 거리가 저장된 배열
dist = [INF] * (V+1)

for i in range(E):
    u,v,w = map(int, input().split(" "))
    edge[u].append([w,v])

# 시작점 초기화
dist[K] = 0
# 시작점 시작점의 가중치는 0이다.
heap = [[0,K]]

# 힙큐가 비지 않을 때까지 반복한다.
while heap:
    # heapq 를 pop 해서 최소 가중치인 가중치와 vertex를 얻는다.
    ew, ev = heapq.heappop(heap)
    # 만약 현재 pop한 값의 가중치가 dist의 가중치와 다르면 바로 다음을 pop 해준다. (최신화 할 필요가 없다, 시간 줄이기 위함, 없어도 됨)
    # 이 부분이 헤깔림
    if dist[ev] != ew: continue
    # 인접 리스트를 확인한다.
    for nw,nv in edge[ev]:
        # 인접 리스트의 값+ 현재 노드의 가중치 값이 dist 배열에 저장된 값보다 작으면 dist 배열을 최신화 해주고 힙에 넣어 준다.
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])

for i in range(1,V+1):
    if dist[i] == INF : print("INF")
    else: print(dist[i])