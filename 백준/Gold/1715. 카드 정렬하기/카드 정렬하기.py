import heapq
import sys

n = int(input())

q = []

# heapq에 다 넣어줌
for _ in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(q, num)

ans = 0
# 1개가 남을 때까지 heapq에서 2개씩 빼서 더하고 다시 넣음
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    ans += a + b
    heapq.heappush(q,a + b)

print(ans)
