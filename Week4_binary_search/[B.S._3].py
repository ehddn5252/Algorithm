# 작성일 : 20201122
# 작성자 : 김동우
# 문제명 : 공유기
# 문제 요약 :
# 1. 도현이 집 N개가 수직선 위에 있다.
# 2. 와이파이를 즐기기 위해 공유기 C개를 설치하려고 한다. 
# 3. 모든 집에서 와이파이를 즐기기 위한 와이파이의 최대 범위는?
# 문제 해설 : 
# 1. 오름차순으로 정렬한다.
# 2. 가장 좌측과 가장 우측 값을 구한다.
# 3. 그 둘사이의 차를 공유기 수로 나누고 변수 compare에 저장.
#    만약 값이 유리수일 경우 올림
# 4. 배열을 한번 돌면서 둘 사이의 간격이 compare보다 작거나 같은 수 중
#    가장 큰 값을 찾는다. 
# 음 .. 뭔 말인지 모르겠다.
import math

def solution():
    x= input().split()
    N=0
    C=0
    inputedList=[]
    N,C=map(int,x)
    for _ in range(N):
        inputedList.append(int(input()))
    
    inputedList.sort()
    compare=0
    ans=0
    compare=math.ceil((inputedList[-1]-inputedList[0])/C)

    if inputedList[1]-inputedList[0]<=compare:
        ans=inputedList[1]-inputedList[0]

    for index,num in enumerate(inputedList):
        if index==0:
            continue

        if num-inputedList[index-1]>compare:
            continue
        else:
            if num-inputedList[index-1]>=ans:
                ans=num-inputedList[index-1]
    print(ans)

if __name__ == "__main__":
    solution()