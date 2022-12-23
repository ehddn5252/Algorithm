# 결혼식

# 친구와 친구의 친구들까지 초대한다.

#
from collections import deque

n = int(input())
m = int(input())
l = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]
visit[1] = True
for _ in range(m):
    start, end = map(int, input().split(" "))
    l[start][end] = 1
    l[end][start] = 1

# 동기라면 추가하고 동기가 아니라면 pass
count = 0
q = deque([[1]])
ans = 0
while count < 2:
    popped = q.popleft()
    queue_list = []
    for k in popped:
        for i, v in enumerate(l[k]):
            if not visit[i] and l[k][i] == 1:
                queue_list.append(i)
                visit[i] = True
                ans += 1
    q.append(queue_list)
    count += 1
visit[1] = False
print(sum(visit))
