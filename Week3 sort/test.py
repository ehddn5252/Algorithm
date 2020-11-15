# 작성일 : 20201113
# 작성자 : 김동우
# 문제명 : 합이 0인 네 정수
# 문제요약 : 배열 4개를 A,B,C,D를 선택해서 A[a] + B[b] + C[c] + D[d] == 0 이되는 순서쌍 구하기

# 문제 해설 :
# 1. 모든 조합을 사용한다면 경우의 수가 너무 많아질듯 어떤 원소를 사용하든 합이 0이 되는 것의 수를 찾기
# 2. 정렬해서 중앙서부터 왼쪽으로가면 마이너스, 오른쪽으로가면 
#  (a,b,c,d)의 쌍이다 a의 집합, b의 집합, c의 집합, d의 집합 이렇게 4개로 나눈다.
# a의 처음부터 시작하면 4000 4000 4000 4000 곱하면 no..
# 질문칸 : solution 2개의 집합으로 나눈다.
#16byte * 16,000,000 = 256,000,000 byte
N=int(input())

inputedList=[]
for _ in range(N):
    inputedList.append(list(map(int,input().split())))

sumFirstSeconddList=[]
for firstNum in inputedList:
    for secondNum in inputedList:
        sumFirstSeconddList.append(firstNum[0]+secondNum[1])

sumThirdFourthList=[]
for thirdNum in inputedList:
    for fourthNum in inputedList:
        sumThirdFourthList.append(thirdNum[2]+fourthNum[3])

sumFirstSeconddList.sort()
sumThirdFourthList.sort()

answer=0
for sumFirstSecondIndex in range(len(sumFirstSeconddList)):
    first=0
    end=len(sumThirdFourthList)-1
    mid=(first+end)//2
    check=0
    while(check<13):
        if sumFirstSeconddList[sumFirstSecondIndex]+sumThirdFourthList[mid]<0:
            first=mid
            mid=(mid+end)//2
        elif sumFirstSeconddList[sumFirstSecondIndex]+sumThirdFourthList[mid]>0:
            end=mid
            mid=(first+mid)//2
        elif sumFirstSeconddList[sumFirstSecondIndex]+sumThirdFourthList[mid]==0:
            answer+=1
            break
        check+=1
print(answer)
