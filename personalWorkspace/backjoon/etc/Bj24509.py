import heapq
from pprint import pprint

stu_num = int(input())
l = [0 for i in range(stu_num+1)]

for _ in range(4):
    heap = []
    subject = list(map(int, input().split(" ")))
    for i in range(stu_num):
        # 최대힙
        heapq.heappush(heap, (-subject[i], i+1))
    pprint(heap)
    while True:
        popped = heapq.heappop(heap)
        if l[popped[1]] == 0:
            l[popped[1]] = 1
            print(popped[1])
            break
