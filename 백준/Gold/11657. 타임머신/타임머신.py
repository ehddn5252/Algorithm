import sys

n, m = map(int, sys.stdin.readline().split(" "))
DEFAULT: int = 10001
l = []
INF = 9999999
distance = [9999999 for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split(" "))
    l.append((a-1,b-1,c))

distance[0]=0

for i in range(n):
    for j in range(m):
        cur_node = l[j][0]
        next_node = l[j][1]
        cost = l[j][2]
        if distance[cur_node] != INF and distance[next_node]>distance[cur_node] + cost:
            distance[next_node] = distance[cur_node] + cost
            if i==n-1:
                print(-1)
                exit()

for i in range(1,n):
    if distance[i]==INF:
        print(str(-1))
    else:
        print(str(distance[i]))