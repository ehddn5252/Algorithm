import sys

n, m = map(int, sys.stdin.readline().split(" "))
ans = 1
for i in range(n, n - m, -1):
    ans *= i

for i in range(2, m + 1):
    ans //= i

print(ans)
