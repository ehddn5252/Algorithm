import copy

n = int(input())

from collections import deque

tmp = deque([n])
q = deque([[n, tmp]])
visit = [0 for i in range(1000001)]
ans_l = []
while q:
    now_n, l = q.popleft()
    if now_n == 1:
        ans_l = l
        break
    if now_n % 3 == 0:
        if not visit[now_n // 3]:
            visit[now_n // 3] = True
            now_n //= 3
            l.append(now_n)
            q.append([now_n, copy.deepcopy(l)])
            now_n *= 3
            l.pop()

    if now_n % 2 == 0:
        if not visit[now_n // 2]:
            visit[now_n // 2] = True
            now_n //= 2
            l.append(now_n)
            q.append([now_n, copy.deepcopy(l)])
            now_n *= 2
            l.pop()
    if now_n != 1:
        if not visit[now_n - 1]:
            visit[now_n - 1] = True
            now_n -= 1
            l.append(now_n)
            q.append([now_n, l])

print(len(ans_l) - 1)
print(" ".join(str(i) for i in ans_l))
