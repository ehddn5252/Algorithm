from collections import deque

N, S, M = map(int,input().split(" "))
l = list(map(int,input().split(" ")))

q = deque([S])
for i in range(len(l)):
    q = deque(list(set(q)))
    q_len = len(q)
    for j in range(q_len):
        popped = q.popleft()
        if popped + l[i]<=M:
            q.append(popped + l[i])
        if popped - l[i] >= 0:
            q.append(popped - l[i])

if len(q)==0:
    print(-1)
else:
    print(max(q))
