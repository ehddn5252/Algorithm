num = int(input())

l = [[999999999 for _ in range(num + 1)] for _ in range(num + 1)]
m = int(input())

for i in range(m):
    start, end, cost = map(int, input().split(" "))
    if l[start][end] > cost:
        l[start][end] = cost
# 여기서부터 플로이드 와샬로 정해야 한다.

for k in range(1, num + 1):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i == j:
                continue
            if l[i][k] + l[k][j] < l[i][j]:
                l[i][j] = l[i][k] + l[k][j]

for i in range(num + 1):
    for j in range(num + 1):
        if l[i][j] == 999999999:
            l[i][j] = 0
l = l[1:]

for i in l:
    i = i[1:]
    print(" ".join(str(j) for j in i))
