from itertools import permutations
import sys

n,m = map(int,sys.stdin.readline().split(" "))

l = sorted(list(map(int,sys.stdin.readline().split(" "))))
tmp_dict = {}
for i in permutations(l,m):
    ret = " ".join(str(j) for j in list(i))
    if not tmp_dict.get(ret):
        tmp_dict[ret]=1
        print(ret)
