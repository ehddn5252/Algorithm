# 작성 일자 : 20210222
# 문제명 : 숫자 카드2
# 문제 요약 : 
# 1 상근이는 숫자 카드 N 개를 들고 있다. 정수 M개가 주어졌을 때, 
# 2. 이 수가 적혀있는 숫자 카드를 상근이가 몇 장 가진지 구하라

# 문제 풀이 : 해쉬 사용한다
# 1. 상근이가 가진 카드 리스트 해쉬를 만든다. 
# 2. 주어진 숫자 리스트를 한바퀴 돌면서 상근이가 가진 카드 리스트 해쉬 값 가져온다.
# 3. O(N)
# 숫자 카드 2
from sys import stdin

def solution(sanggnCardList,numberCardList):
    sanggnHash={}
    answer=""
    # 1. 상근이가 가진 카드 리스트 해쉬를 만든다. 
    for sanggnCard in sanggnCardList:
        if sanggnHash.get(sanggnCard,0)==0:
            sanggnHash[sanggnCard]=1
        else:
            sanggnHash[sanggnCard]+=1

    # 2. 주어진 숫자 리스트를 한바퀴 돌면서 상근이가 가진 카드 리스트 해쉬 값 가져온다.
    for numberCard in numberCardList:
        # sanggnHash.get(numberCard,0)는 만약 sanggnHash[numberCard]가 존재하면 그 value 아니면 0을 반환
        if sanggnHash.get(numberCard,0)==0:
            answer+=" 0"
        else:
            answer+=f' {sanggnHash[numberCard]}'
    print(answer[1:])


if __name__=="__main__":
    arraySize=int(stdin.readline().strip())
    sanggnCardList=list(map(int,stdin.readline().split()))
    K=int(stdin.readline().strip())
    numberCardList=list(map(int,stdin.readline().split()))
    solution(sanggnCardList,numberCardList)