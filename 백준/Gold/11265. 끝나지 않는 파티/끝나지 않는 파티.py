N, M = map(int, input().split(" "))
l = []
for i in range(N):
    l.append(list(map(int, input().split(" "))))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if l[i][k] + l[k][j] < l[i][j]:
                l[i][j] = l[i][k] + l[k][j]

for i in range(M):
    A, B, C = map(int, input().split(" "))
    A = A - 1
    B = B - 1
    if l[A][B] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")
