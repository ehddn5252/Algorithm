n = int(input())

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

map1 = {1: 0, -1: 0, 0: 0}


def recur(start_i, start_j, offset):
    if offset == 1:
        map1[l[start_i][start_j]] += 1
        return
    first = l[start_i][start_j]
    divided = offset // 3
    for i in range(start_i, start_i + offset):
        for j in range(start_j, start_j + offset):
            if l[i][j] != first:
                recur(start_i, start_j, divided)
                recur(start_i + divided, start_j, divided)
                recur(start_i, start_j + offset // 3, divided)
                recur(start_i + divided * 2, start_j, divided)
                recur(start_i, start_j + divided * 2, divided)
                recur(start_i + divided, start_j + divided, divided)
                recur(start_i + divided * 2, start_j + divided, divided)
                recur(start_i + divided, start_j + divided * 2, divided)
                recur(start_i + divided * 2, start_j + divided * 2, divided)
                return
    map1[l[start_i][start_j]] += 1


recur(0, 0, n)
print(map1[-1])
print(map1[0])
print(map1[1])
