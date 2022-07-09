import heapq
from pprint import pprint
from collections import deque
stu_num = int(input())
l = [0 for i in range(stu_num+1)]
korean = []
english = []
math = []
science = []


for _ in range(stu_num):
    subject = list(map(int, input().split(" ")))
    heapq.heappush(korean, (-subject[1], subject[0]))
    heapq.heappush(english, (-subject[2], subject[0]))
    heapq.heappush(math, (-subject[3], subject[0]))
    heapq.heappush(science, (-subject[4], subject[0]))

heapq_l = deque([korean, english, math, science])
for _ in range(4):
    subject = heapq_l.popleft()
    while True:
        popped = heapq.heappop(subject)
        if l[popped[1]]==0:
            l[popped[1]] = 1
            print(str(popped[1])+" ",end="")
            break