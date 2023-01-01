import sys

N, M = map(int, sys.stdin.readline().split(" "))
N_l = {}
l = list(map(int, sys.stdin.readline().split(" ")))
for i in range(N):
    N_l[l[i]] = 1
ans = N

l = list(map(int, sys.stdin.readline().split(" ")))

for j in range(M):
    if N_l.get(l[j]) != 1:
        ans += 1
    else:
        ans -= 1
print(ans)
