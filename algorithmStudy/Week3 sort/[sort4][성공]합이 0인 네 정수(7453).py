# 작성일 : 20201113
# 작성자 : 김동우
# 문제명 : 합이 0인 네 정수
# 문제요약 : 배열 4개를 A,B,C,D를 선택해서 A[a] + B[b] + C[c] + D[d] == 0 이되는 순서쌍 구하기

# 문제 해설 :
# 1. 모든 조합을 사용한다면 경우의 수가 너무 많아질듯 어떤 원소를 사용하든 합이 0이 되는 것의 수를 찾기

# 해결방법 :  (https://suri78.tistory.com/169) 참고
# 0. 0,1,2,3 인덱스에 있는 값을 각각의 인덱스 리스트에 추가한다. firstList, secondList, thirdList, fourthList 
# 1. 0번째, 1번째 인덱스를 더한 값을 key로, 2번째, 3번째 인덱스를 key로 하는 2개의 딕셔너리로 나눈다. sumFirstSecondDic, sumThirdFourthDic
# 2. sumFirstSecondDic를 돌면서 sumFirstSecondDic의 key값이 sumThirdFourthDic의 key값*-1 인 경우가 존재할 경우 그 경우를 ans에 추가한다.
# key value로 저장하면 겹치는 경우를 제외하기 때문에 메모리를 덜 먹어서 해결되는건가?.
# 시간 복잡도 : O(N^2)) 

def solution():
    N=int(input())

    inputedList=[]
    firstList=[]
    secoondList=[]
    thirdList=[]
    fourthList=[]
    # 0. 0,1,2,3 인덱스에 있는 값을 각각의 인덱스 리스트에 추가한다. firstList, secondList, thirdList, fourthList 
    for _ in range(N):
        inputedList=list(map(int,input().split()))
        firstList.append(inputedList[0])
        secoondList.append(inputedList[1])
        thirdList.append(inputedList[2])
        fourthList.append(inputedList[3])

    sumFirstSecondDic={}
    for first in firstList:
        for second in secoondList:
            # 여기서 없을 시에 초기화를 자동으로 실행 한다.
            if not sumFirstSecondDic.get(first+second):
                sumFirstSecondDic[first+second] = 1
            else:
                sumFirstSecondDic[first+second] += 1

    sumThirdFourthDic = {}
    for third in thirdList:
        for fourth in fourthList:
            # sum34에 key가 third+fourth인 dic이 없을 시에 초기화를 자동으로 실행 한다.
            if not sumThirdFourthDic.get(third+fourth):
                sumThirdFourthDic[third+fourth] = 1
            # 만약 있으면 개수를 추가한다. 
            else:
                sumThirdFourthDic[third+fourth] += 1
    ans=0
    # sum12를 돌면서 sum12의 key값이 sum34의 -1 * key 가 존재하면 그 수를 ans에 추가한다. (해시)
    for key in sumFirstSecondDic:
        if sumThirdFourthDic.get(-key):
            ans += (sumFirstSecondDic[key]*sumThirdFourthDic[-key])
    print(ans)

if __name__ == "__main__":
    solution()