import heapq
import sys
print = sys.stdout.write
n = int(sys.stdin.readline())
l = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(l, (abs(num), num))
    else:
        if l:
            tmp = heapq.heappop(l)
            print(str(tmp[1])+"\n")
        else:
            print(str(0)+"\n")
