from itertools import permutations, combinations
import sys

n, m = map(int, sys.stdin.readline().split(" "))

l = [ i+1 for i in range(n) ]

for i in combinations(l,m):
    print(" ".join(str(s) for s in i))