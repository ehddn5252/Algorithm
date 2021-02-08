# 파이썬 heap 모듈 heapq 사용법
import heapq

# 최소 힙 생성
heap = []

# 힙에 원소 추가
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

# 힙에서 원소 삭제
print(heapq.heappop(heap))
print(heap)
# 최소값 삭제하지 않고 얻기
print(heap[0])

# 기존 리스트를 힙으로 변환
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)

# [응용] 최대 힙

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1

# [응용] K번째 최소값/최대값

def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))

# [응용] 힙 정렬

def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  
  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))