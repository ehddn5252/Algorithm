import copy
from collections import deque

subin, bro = map(int, input().split(" "))

visit = [False for i in range(100001)]
visit[subin] = True
result = 100001
if subin==bro:
    print(0)
    print(1)
else:
    q = [[subin, 0]]
    q = deque(q)
    result_count = 0
    while q:
        popped = q.popleft()
        visit[popped[0]] = True

        if popped[0] == bro and popped[1] < result:
            result = popped[1]
            result_count = 1
            continue

        elif popped[0] == bro and popped[1] == result:
            result_count += 1
            continue

        if popped[0] + 1 <= 100000 and visit[popped[0] + 1] is False:
            q.append([popped[0] + 1, popped[1] + 1])

        if popped[0] - 1 >= 0 and visit[popped[0] - 1] is False:
            q.append([popped[0] - 1, popped[1] + 1])

        if popped[0] * 2 <= 100000 and visit[popped[0] * 2] is False:
            q.append([popped[0] * 2, popped[1] + 1])

    print(result)
    print(result_count)
