# 작성일 : 20201201
# 작성자 : 김동우
# 문제명 : 블랙잭
# 문제 요약 :
# 1. 카드 뭉치에서 3장을 골라서 M보다 작거나같은 수를 만들고 그 수를 출력하라.
#  
# 문제 본문은 contents.md 참고 

# 문제 해설 : 
# 처음부터 끝까지 돌면 100^3 = 1,000,000 100번이라 시간은 가능하다

# 시간 복잡도 : O(N^3)


def solution():
    N,M=map(int,input().split())
    cardList=[]
    cardList=list(map(int,input().split()))
    cardList.sort()
    max=0
    sum=0
    cardSize=len(cardList)
    for firstCard in range(0,cardSize):
        for secondCard in range(firstCard+1,cardSize):
            for thirdCard in range(secondCard+1,cardSize):
                sum=cardList[firstCard]+cardList[secondCard]+cardList[thirdCard]
                if(sum==M):
                    print(M)
                    return
                if sum<M and sum>max:
                    max=sum
    print(max)
                

if __name__ == "__main__":
    solution()