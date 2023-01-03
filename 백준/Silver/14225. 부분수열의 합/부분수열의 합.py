from itertools import combinations

N = int(input())
map1 = [0 for i in range(2000001)]
l = list(map(int, input().split(" ")))

for i in l:
    map1[i] = 1
for i in range(2, len(l)+1):
    for j in combinations(l, i):
        map1[sum(j)] = 1

for i in range(1, len(map1)):
    if map1[i] == 0:
        print(i)
        break
