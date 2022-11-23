N, M = map(int, input().split(" "))
l1 = []
for i in range(N):
    l1.append(list(map(int, input().split(" "))))

for i in range(N):
    tmp = list(map(int, input().split(" ")))
    for j, j_value in enumerate(tmp):
        if j == len(tmp) - 1:
            print(l1[i][j] + tmp[j], end="\n")
        else:
            print(l1[i][j] + tmp[j], end=" ")
