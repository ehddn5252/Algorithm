import sys
from itertools import combinations
X = input()
Y = input()
Z = input()
k = int(input())

X_l = [i for i in X]
Y_l = [i for i in Y]
Z_l = [i for i in Z]
ll = [X_l,Y_l,Z_l]
dic = {}
answer_list = []
for index, com in enumerate(ll):
    for i in combinations(com, k):
        key = "".join(i)
        if key in dic.keys():
            answer_list.append(key)
        else:
            dic[key] = 1
s = list(set(answer_list))
s.sort()


for i in s:
    print(i)
if s==[]:
    print(-1)