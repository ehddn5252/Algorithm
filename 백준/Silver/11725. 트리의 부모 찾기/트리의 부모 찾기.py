import sys
from collections import deque

num = int(input())
parent = [0 for i in range(num + 1)]
visit = [False for i in range(num + 1)]
l = [[] for i in range(num + 1)]
for child in range(num-1):
    A, B = map(int, sys.stdin.readline().split(" "))
    l[A].append(B)
    l[B].append(A)

q = deque([1])
while q:
    parent_node = q.popleft()
    visit[parent_node] = True

    for child in l[parent_node]:
        if not visit[child]:
            q.append(child)
            parent[child] = parent_node


for i,v in enumerate(parent):
    if i==0 or i==1:
        continue
    print(parent[i])