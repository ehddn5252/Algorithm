from collections import deque
import sys

N,K=map(int, sys.stdin.readline().split())
MAX=100001
arr=[-1] * MAX
q=deque()
q.append(N)
arr[N]=0
while q:
    x= q.popleft()
    if x==K:
        print(arr[K])
        break
    for i in (2*x,x-1,x+1):
        if 0 <= i < MAX and arr[i]==-1:
                if i==2*x:
                    arr[i]=arr[x]
                    q.append(i)
                else:
                    arr[i]=arr[x]+1
                    q.append(i)