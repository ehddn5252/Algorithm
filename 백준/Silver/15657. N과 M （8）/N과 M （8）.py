from itertools import combinations_with_replacement
import sys

n,m = map(int,sys.stdin.readline().split(" "))

l = sorted(list(map(int,sys.stdin.readline().split(" "))))

for i in combinations_with_replacement(l,m):
    print(" ".join(str(j) for j in list(i)))
