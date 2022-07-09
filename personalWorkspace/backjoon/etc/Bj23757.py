import heapq

N, M = map(int, input().split(" "))
heap = []

N_l = list(map(int, input().split(" ")))
M_l = list(map(int, input().split(" ")))

for i in N_l:
    heapq.heappush(heap, (-i,i))

index = 0
while index<len(M_l):
    popped = heapq.heappop(heap)
    get_present = popped[1] - M_l[index]
    if get_present < 0:
        print(0)
        break
    else:
        heapq.heappush(heap, (-get_present,get_present))
        index += 1

if index == len(M_l):
    print(1)
