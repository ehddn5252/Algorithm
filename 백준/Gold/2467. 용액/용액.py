
import sys
n = int(input())

l = list(map(int, sys.stdin.readline().split(" ")))
INF = 2000000000
start = 0
ans = INF
ans1 = 0
ans2 = 0
start = 0
end = len(l)-1

while start < end:
    if abs(l[start]) > abs(l[end]):
        if ans > abs(l[end] + l[start]):
            ans1 = l[start]
            ans2 = l[end]
            ans = abs(l[end] + l[start])
        start += 1
    elif abs(l[start]) < abs(l[end]):
        if ans > abs(l[end] + l[start]):
            ans1 = l[start]
            ans2 = l[end]
            ans = abs(l[end] + l[start])
        end -= 1
    elif (l[end] + l[start]) == 0:
        ans1 = l[start]
        ans2 = l[end]
        break
print(ans1)
print(ans2)
