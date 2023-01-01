import sys

N, M = map(int, sys.stdin.readline().split(" "))
N_l = {}
M_l = []
ans = 0
for i in range(N):
    N_l[sys.stdin.readline()] = 1
for i in range(M):
    M_l.append(sys.stdin.readline())

for j in range(M):
    if N_l.get(M_l[j]) == 1:
        ans += 1
print(ans)
