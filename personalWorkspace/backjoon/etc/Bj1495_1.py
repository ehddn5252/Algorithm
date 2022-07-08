N, S, M = map(int, input().split(" "))
l = list(map(int, input().split(" ")))
nq = [S]

for i in range(len(l)):
    q = list(nq)
    nq = set([])
    for _ in range(len(q)):
        popped = q.pop()
        if popped + l[i] <= M:
            nq.add(popped + l[i])
        if popped - l[i] >= 0:
            nq.add(popped - l[i])

if len(nq) == 0: print(-1)
else: print(max(nq))
