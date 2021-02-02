# 작성일 : 20201126
# 작성자 : 김동우
# 문제명 : 랜선 자르기
# 문제 요약 : 
#  배열 n개를 k개로 잘라서 만들 수 있는 최대 길이는?
# 문제 해석 :
# 방법 1
# 1. 배열 중 가장 큰 값을 end값으로 정하고 이분탐색한다.
# 2. mid 값으로 자르고 그렇게 생긴 랜선의 수를 ans라하면
# 2-1. 그 수가 자르는 수고 목표보다 크면 ( 더많은 수로 잘리면) 랜선의 최대 길이를 늘린다.
# 2-2. 



def solution():
    n,objectLanNum=map(int,input().split())
    inputedList=[]
    for _ in range(n):
        inputedList.append(int(input()))

    max=0
    for i in inputedList:
        if(max<i):
            max=i

    start=1
    end=max

    while(start<=end):
        mid=(start+end)//2
        LANCount=0
        for num in inputedList:
            LANCount+=num//mid
            # 잘라서 나온 
            if LANCount>objectLanNum:
                start=mid+1
            elif LANCount==objectLanNum:
                ans=mid
                start=mid+1
            else:
                end=mid-1

    print(ans)




if __name__ == "__main__":
    solution()