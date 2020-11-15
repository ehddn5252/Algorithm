# 작성일 : 20201113
# 작성자 : 김동우
# 문제명 : 합이 0인 네 정수
# 문제요약 : 배열 4개를 A,B,C,D를 선택해서 A[a] + B[b] + C[c] + D[d] == 0 이되는 순서쌍 구하기

# 문제 해설 :
# 1. 모든 조합을 사용한다면 경우의 수가 너무 많아질듯 어떤 원소를 사용하든 합이 0이 되는 것의 수를 찾기

# 질문 본 후 : solution 2개의 집합으로 나눈다.
#16byte * 16,000,000 = 256,000,000 byte
# 실패 요인 : 메모리 초과

def solution():
    N=int(input())

    inputedList=[]
    firstList=[]
    secoondList=[]
    thirdList=[]
    fourthList=[]
    for i in range(N):
        inputedList=list(map(int,input().split()))
        firstList.append(inputedList[0])
        secoondList.append(inputedList[1])
        thirdList.append(inputedList[2])
        fourthList.append(inputedList[3])

    sumFirstSeconddList=[]

    for firstNum in firstList:
        for secondNum in secoondList:
            sumFirstSeconddList.append(firstNum+secondNum)

    sumThirdFourthList=[]
    for thirdNum in thirdList:
        for fourthNum in fourthList:
            sumThirdFourthList.append(thirdNum+fourthNum)

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

if __name__ == "__main__":
    solution()