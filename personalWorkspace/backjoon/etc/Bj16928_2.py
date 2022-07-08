import sys
read = lambda : sys.stdin.readline()

n, m = map(int, read().split(" "))
dist = [-1] * 101
dic = {}
for _ in range(n+m):
    u, v = map(int, read().split(" "))
    dic[u] = v
queue = []
for i in range(2, 8):
    if i in dic:
        dist[dic[i]] = 1
        queue.append(dic[i])
    else:
        dist[i] = 1
        queue.append(i)
dist[0]=0
dist[1]=0

while queue:
    x = queue.pop(0)
    if x == 100:
        print(dist[100])
        break
    for i in range(1, 7):
        if 1<= x+i <= 100:
            if x+i not in dic:
                if dist[x+i] == -1 or dist[x+i] > dist[x]+1:
                    queue.append(x+i)
                    dist[x+i] = dist[x]+1
            else:
                xi = dic[x+i]
                if dist[xi] == -1 or dist[xi] > dist[x]+1:
                    queue.append(xi)
                    dist[xi] = dist[x]+1