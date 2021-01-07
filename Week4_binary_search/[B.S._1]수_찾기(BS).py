# 작성일 : 20201126
# 작성자 : 김동우
# 문제명 : 수 찾기
# 문제 요약 :
# 0. 배열2와 배열1이 주어진다. 배열 1에 배열 2에 있는 수가 있는 지 확인하고 있으면 1 없으면 0을 출력

# 문제 해설 : 
# 방법 2: 이분 탐색
# 0. 배열 2를 오름 차순으로 정렬한다.
# 1. 배열 1에 있는 값(list1Value)을 차례로 선택한다.
# 2. 이분탐색으로 배열 2와 비교한다. (start<=end)
# 2-1. list1Value와 배열 2의 중간 값과 비교한다.  
# 2-2. list1Value가 중간 값보다 크다면 start=mid+1로 
# 2-3. list1Value가 중간 값보다 작다면 end=mid-1로 두고 비교한다.
# 2-4. listValue==mid라면 존재하는 것으로 리스트에 1을 추가
# 2-5. start<=end인 동안에 없다면 0을 추가
# 시간 복잡도 : O(N*log_2(N))

N=0
inputedList1=[]
M=0
inputedList2=[]
# local함수에서 초기화를 하면 전역 변수라도 적용이 안된다.
def solution():
    int(input())
    inputedList2=list(map(int,input().split()))
    int(input())
    inputedList1=list(map(int,input().split()))

    inputedList2.sort()
    ansList=[]
    for list1Num in inputedList1:
        start=0 
        end=len(inputedList2)-1
        while (start<=end):
            mid=(start+end)//2

            if inputedList2[mid]==list1Num:
                ansList.append(1)
                break
            elif inputedList2[mid]<list1Num:
                start=mid+1
            elif inputedList2[mid]>list1Num:
                end=mid-1

        if start>end:
            ansList.append(0)

    for i in ansList:
        print(i)

if __name__ == "__main__":
    solution()