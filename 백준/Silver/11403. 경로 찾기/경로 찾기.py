n = int(input())

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if l[i][k] == 1 and l[k][j] == 1:
                l[i][j] = 1


for i in range(n):
    print(" ".join(str(j) for j in l[i]))
