# 작성일자 : 20210212
# 문제명 : 동전 1 (백준 2293)

# 문제 요약 : 1. n가지 종류의 동적이 있다. 각각의 동전이 나타내는 가치는 다르다.
#             2. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.
#             3. 입력으로 n 과 k 다음 n줄에는 각각의 동전의 가치가 주어진다.


# 문제 풀이 : 1. 백트레킹으로 모든 경우의 수를 확인한다.
#             2.
# 항상 얕은 복사와 깊은 복사를 생각해야 한다.
# 아래와 같이 백트레킹으로 할 시에 RecursionError: maximum recursion depth exceeded in comparison 런타임 에러가 발생한다.
# 런타임을 없애기 위해 sys.setrecursionlimit(10**7)을 사용하면 시간초과가 뜬다 -> 동적 계획법으로 다시풀자
import sys
sys.setrecursionlimit(10**7)
answer=0
answerKindList=[]

def recur(currentCoinSum,coinKindsDic):
    global answer
    if currentCoinSum==k:
        if coinKindsDic not in answerKindList:
            dic1=coinKindsDic.copy()
            answerKindList.append(dic1)
            answer+=1 
        return
    elif currentCoinSum>k:
        return

    for i in coinList:
        currentCoinSum+=i
        coinKindsDic[i]+=1
        recur(currentCoinSum,coinKindsDic)
        coinKindsDic[i]-=1
        currentCoinSum-=i


if __name__=="__main__":

    n,k=map(int,sys.stdin.readline().split())
    global coinList
    coinList=[]
    coinKindsDic={}
    for i in range(n):
        coinkind=int(sys.stdin.readline())
        coinList.append(coinkind)
        coinKindsDic[coinkind]=0

    for i in coinList:
        coinKindsDic[i]+=1
        recur(i,coinKindsDic)
        coinKindsDic[i]-=1
    print(f'{answer}')