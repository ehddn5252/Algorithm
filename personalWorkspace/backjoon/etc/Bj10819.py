import sys

num = int(sys.stdin.readline())

l = list(map(int,input().split(" ")))

'''
6
20 1 15 8 4 10
로 들어오면

8 20 1 15 4 10 로 둬야 최댓값이 나온다.
그냥 permutation 돌리자.

'''
from itertools import permutations

max_ans = 0
for new_l in permutations(l,len(l)):
    tmp = 0
    for j in range(0,len(new_l)-1):
        tmp+=abs(new_l[j]-new_l[j+1])
    if tmp>max_ans:
        max_ans = tmp
print(max_ans)
