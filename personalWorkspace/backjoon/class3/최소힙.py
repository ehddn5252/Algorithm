# 작성일자 : 20210215
# 문제명 : 최소힙 [백준 1927]

from sys import stdin
import heapq
if __name__=="__main__":
    times=int(stdin.readline())
    heap=[]
    for i in range(times):
        num=int(stdin.readline())
        if num==0:
            try:
                print(heapq.heappop(heap))
            except:
                print(0)
        else:
            heapq.heappush(heap,num)
        