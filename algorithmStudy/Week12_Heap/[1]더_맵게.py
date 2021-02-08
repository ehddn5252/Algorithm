# 작성일자 : 20210208
# 문제명 : 더 맵게 (heap)
# 문제 요약 : 음식의 스코빌 지수 리스트와 최소 스코빌 지수가 주어진다.
# 스코빌 리스트에 있는 음식 2개를 섞으면 
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2) 가 된다.
# 리스트에 있는 모든 음식의 스코빌 지수가 k 이상이 되려면 몇 번 섞어야 하는가?

import heapq

def solution(scoville, K):
    heap = []
    for index,value in enumerate(scoville):
        heapq.heappush(heap, value)
    mixCount = 0
    while True:
        if heap[0]>=K:
            return mixCount
        if len(heap)==1:
            return -1
        mostNotSpicy=heapq.heappop(heap)
        secondNotSpicy=heapq.heappop(heap)
        mixedFood=mostNotSpicy+secondNotSpicy*2
        heapq.heappush(heap,mixedFood)
        mixCount+=1




if __name__=="__main__":
    scoville=[1, 2, 3, 9, 10, 12]
    K=7
    solution(scoville,K)
    # return = 2