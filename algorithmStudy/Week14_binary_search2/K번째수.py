# 작성 일자 : 20210222
# 문제명 : K번째 수
# 문제 요약 : 
# 1. 세준이는 크기가 N x N인 배열 A를 만들었다. 
# 2. 배열에 들어있는 수 A[i][j]=i x j 이다.
# 3. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N x N이 된다. 
# 4. B를 오름차순 정렬했을 때 B[k]를 구해보자.


# 문제 풀이 :
# 1. (1 * 1 2 * 1 + .. + n * 1 )+ (1 * 2 + 2 * 2 + .. + n * 2) + ... (n * 1 n * 2 + .. + n * n) 데이터를 만들어야 한다.
# 1-1. 이는 2중 for문으로 최대 100,000,000 회(1억) 돈다.
# 1-2( 2중 for문 리스트 쓰면 메모리 초과 )
# 2. 이진 탐색한다.
# 3. start=1,찾는 수를 end 로 두고 mid=(start+end)//2 로 둔다.
# 4. mid를 1부터 N까지 i로 나눈 것들의 합이 mid 값보다 아래에 있는 값의 수가 된다.
# 4-1. 왜냐하면 문제에서 mid 값과 비교하는데, 그걸 1부터 N까지 각 수로 나눈 것이 mid보다 작은 것의 된다.

from sys import stdin

def solution(arraySize,K):
    start=1
    end=K
    answer=0
    while start<=end:
        mid=(start+end)//2
        count=0
        for i in range(1,arraySize+1):
            # 이거 첨에 우째 생각해내냐? ㄷㄷ 
            count+=min(mid//i,arraySize)
        if count>=K:
            answer=mid
            end=mid-1
        elif count<K:
            start=mid+1
    print(answer)




if __name__=="__main__":
    arraySize=int(stdin.readline().strip())
    K=int(stdin.readline().strip())
    solution(arraySize,K)
