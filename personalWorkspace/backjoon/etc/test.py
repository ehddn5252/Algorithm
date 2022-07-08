import sys

INF = 10 * 20000
pq=[]
V, E = map(int,sys.stdin.readline().split(" "))
start_node = int(sys.stdin.readline())
adj = [[0 for i in range(V)] for i in range(V)]
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split(" "))
    adj[s - 1][e - 1] = w

visit = [ False for i in range(V)]
distance = [ INF for i in range(V)]
distance[start_node - 1] = 0
visit[start_node - 1] = True
current = 0

for i in range(V):
    min = INF
    for j in range(V):
        # 주변 노드 중 최소 비용 노드를 찾는다.
        # 이 부분을 heapq 로 바꿀 수 있다
        if visit[j] == False and distance[j]<min:
            min = distance[j]
            current = j

    visit[current] = True
    # 최소 비용 노드에서 다른 노드로 가는 비용을 넣는다.
    for j in range(V):
        if not visit[j] and adj[current][j]!=0 and adj[current][j]+distance[current]<distance[j]:
            distance[j] = adj[current][j] + distance[current]

for i in range(distance):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
