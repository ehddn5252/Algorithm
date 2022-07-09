import sys

'''
3 3
10 3
3 2
9 1
3 0
'''

num,n = map(int,sys.stdin.readline())

l = []
for i in range(num+1):
     l.append(list(map(int,sys.stdin.readline())))



def recur(n,l):
    for i in range(l):
        return recur(n,l)