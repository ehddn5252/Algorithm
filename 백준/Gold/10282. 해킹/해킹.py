testcase = int(input())
import sys
import heapq

for _ in range(testcase):
    n, d, c = map(int, input().split(" "))  # 컴퓨터 개수, 의존성 개수, 해킹 컴퓨터 번호
    l = [[] for _ in range(n + 1)]
    for i in range(d):
        a, b, t = map(int, sys.stdin.readline().split())
        l[b].append((t, a))
    visit = [False for _ in range(n + 1)]
    q = [(0, c)]  # (time, computer number)
    max_times=0
    while q:
        time, c_n = heapq.heappop(q)
        if visit[c_n]:
            continue
        visit[c_n] = True
        if time > max_times:
            max_times=time
        for i, v in enumerate(l[c_n]):
            if not visit[v[1]]:
                heapq.heappush(q, (time + v[0], v[1]))
    print(f'{sum(visit)} {max_times}')
