"""
1. 처음 감염된 컴퓨터로 BFS 돌린다.

"""
import heapq

tc = int(input())

for _ in range(tc):
    n, d, c = map(int, input().split(" "))  # 컴퓨터 수, 의존성 개수, 해킹 당한 컴퓨터 수
    l = [[] for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]
    for t in range(d):
        a, b, s = map(int, input().split(" "))  # 컴퓨터 수, 의존성 개수, 해킹 당한 컴퓨터 수
        l[b].append((s,a))

    q = [(0, c)]
    heapq.heapify(q)
    max_times = 0
    while q:
        time,node = heapq.heappop(q)
        if visit[node]:
            continue
        else:
            visit[node]=True
        if time > max_times:
            max_times = time

        for i in l[node]:
            if not visit[i[1]]:
                heapq.heappush(q, (time + i[0],i[1]))
    print(str(sum(visit)) + " " + str(max_times))
