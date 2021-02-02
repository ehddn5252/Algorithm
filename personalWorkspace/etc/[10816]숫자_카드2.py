# 작성일자 20210202
# 문제명 : 백준 [10816] 숫자 카드 2
# 문제 요약 : 
# 상근이가 n장의 카드를 가지고 있다.
# 랜덤 숫자 카드 목록 m개 안에 상근이가 가지고 있는 숫자 카드가 존재하는 지 보고 몇개 존재하는 지 찾기
# 2중 for문을 사용하면 500,000 제곱이라 시간초과가 난다.
# for문 하나로 해결해야 한다.
import sys


def solution(sangguenCardList,cardList):
    hashDictionary={}
    for card in cardList:
        hashDictionary[card]=0
        
    for card in sangguenCardList:
        if card in hashDictionary:
            hashDictionary[card]+=1
    ansString=""
    for card in cardList:
        ansString+=str(hashDictionary[card])+" "
    print(ansString)
        



if __name__=="__main__":
    sangguenCardNum=int(sys.stdin.readline())
    sangguenCardList=list(map(int,sys.stdin.readline().split()))
    cardNum=int(sys.stdin.readline())
    cardList=list(map(int,sys.stdin.readline().split()))

    solution(sangguenCardList,cardList)