# 작성 일자 : 20210222
# 문제명 : K번째 수
# 문제 요약 : 
# 1. 세준이는 크기가 N x N인 배열 A를 만들었다. 
# 2. 배열에 들어있는 수 A[i][j]=i x j 이다.
# 3. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N x N이 된다. 
# 4. B를 오름차순 정렬했을 때 B[k]를 구해보자.

# 문제 풀이 : 
# 1. (1 * 1 2 * 1 + .. + n * 1 )+ (1 * 2 + 2 * 2 + .. + n * 2) + ... (n * 1 n * 2 + .. + n * n) 데이터를 만들어야 한다.
# 1-1. 이는 2중 for문으로 최대 100,000,000 회 돌자.
# 우선순위 큐를 사용해서 해결한다.
# 2. heapq를 만들어 거기에 넣는다. 
# 3. 메모리 초과가 뜬다.
# 4. 

from sys import stdin
import heapq

def solution(arraySize,K):
    heapB=[]
    for i in range(1,arraySize+1):
        for j in range(1,arraySize+1):
            heapq.heappush(heapB,i*j)

    for i in range(K-1):
        heapq.heappop(heapB)
    print(heapq.heappop(heapB))


if __name__=="__main__":
    arraySize=int(stdin.readline().strip())
    K=int(stdin.readline().strip())
    solution(arraySize,K)
