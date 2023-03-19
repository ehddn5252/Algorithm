import sys

N, M = map(int, sys.stdin.readline().split(" "))
l = []
start = 0

max_value = 1000000001
for i in range(N):
    a, b = map(str, sys.stdin.readline().split(" "))
    l.append([int(b), a])

start = 0
end = 0

for i in range(M):
    input_num = int(sys.stdin.readline())
    ans=l[0][1]
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if l[mid][0] >= input_num:
            end = mid - 1
        else:
            ans = l[mid][1]
            start = mid + 1
    print(l[start][1])