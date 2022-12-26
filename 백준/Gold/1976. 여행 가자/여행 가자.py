import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

l = [list(map(int, input().split(" "))) for _ in range(n)]

calender = list(map(int, input().split(" ")))

for i in range(n):
    l[i][i]=1

for k in range(n):
    for i in range(n):
        if i==k:continue
        for j in range(n):
            if i == j: continue
            if l[i][k] == 1 and l[k][j] == 1:
                l[i][j] = 1

start = calender[0]
for i, v in enumerate(calender):
    if i == 0:
        continue
    if l[start - 1][v - 1] == 1:
        start = v
    else:
        print("NO")
        exit()
print("YES")
