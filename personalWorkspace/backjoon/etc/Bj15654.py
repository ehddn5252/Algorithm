from itertools import permutations

N, M = map(int,input().split(" "))
l = list(map(int,input().split(" ")))

l.sort()
for i in permutations(l,M):
    for j in i:
        print(str(j)+" ",end="")
    print()