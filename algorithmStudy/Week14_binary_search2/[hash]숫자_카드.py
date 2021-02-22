# 작성 일자 : 20210222
# 문제명 : 숫자 카드
# 문제 요약 : 
# 1 상근이는 숫자 카드 N 개를 들고 있다. 정수 M개가 주어졌을 때, 
# 2. 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는 지 아닌 지 구하라

# 문제 풀이 : 
# 1. 해쉬 사용한다
from sys import stdin

def solution(sanggnCardList,numberCardList):
    sanggnHash={}
    answer=""
    for sanggnCard in sanggnCardList:
        sanggnHash[sanggnCard]=1
    for numberCard in numberCardList:
        if sanggnHash.get(numberCard,0)==0:
            answer+=" 0"
        else:
            answer+=" 1"
    print(answer[1:])


if __name__=="__main__":
    arraySize=int(stdin.readline().strip())
    sanggnCardList=list(map(int,stdin.readline().split()))
    K=int(stdin.readline().strip())
    numberCardList=list(map(int,stdin.readline().split()))
    solution(sanggnCardList,numberCardList)
