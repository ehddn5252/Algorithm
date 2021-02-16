# 작성일자 : 20210216
# 문제명 : 이중 우선순위 큐
# 문제 요약: 이중 우선순위 큐 구현

import heapq
from sys import stdin

if __name__=="__main__":
    testcase=int(stdin.readline())
    for _ in range(testcase):
        operatorNum=int(stdin.readline().strip())
        maxHeap=[]
        minHeap=[]
        insertSize=0
        for _ in range(operatorNum):
            operator=stdin.readline().strip()
            if operator[0]=="I":
                num=int(operator[2:])
                heapq.heappush(maxHeap,-num)
                heapq.heappush(minHeap,num)
                insertSize+=2
            elif operator=="D 1":
                if insertSize!=(len(maxHeap)+len(minHeap))*2:
                    heapq.heappop(maxHeap)
                else:
                    insertSize=0
                    maxHeap=[]
                    minHeap=[]
            elif operator=="D -1":
                if insertSize!=(len(maxHeap)+len(minHeap))*2:
                    heapq.heappop(minHeap)
                else:
                    insertSize=0
                    maxHeap=[]
                    minHeap=[]
        if insertSize!=(len(maxHeap)+len(minHeap))*2:
            print(f'{-heapq.heappop(maxHeap)} {heapq.heappop(minHeap)}')
        else:
            print(f'EMPTY')