import sys
import copy
N, M = map(int, sys.stdin.readline().split(" "))

l = []
l2 = []

for i in range(N):
    inner_l = list(map(int, sys.stdin.readline().split(" ")))
    l.append(inner_l)
    l2.append(copy.deepcopy(inner_l))

for i in range(0, N):
    for j in range(1, N):
        l[i][j] = l[i][j - 1] + l[i][j]

for i in range(0, N):
    for j in range(1, N):
        l[j][i] = l[j][i] + l[j - 1][i]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(" "))
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    t1=0
    t2=0
    t3=0
    if x1==x2 and y1==y2:
        print(l2[x1][y1])
    else:
        if x1!=0:
            t1=l[x1-1][y2]
        if y1!=0:
            t2 = l[x2][y1-1]
        if x1!= 0 and y1 != 0:
            t3 = l[x1-1][y1-1]
        print(l[x2][y2] - t1 - t2 + t3)
