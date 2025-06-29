# 작성일자 : 20210212
# 문제명 : 동전 1 (백준 2293)

# 문제 요약 : 1. N가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다.
#             2. 이 동전을 적당히 사용해서, 그 가치의 합이 K원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.
#             3. 입력으로 N 과 K 다음 N줄에는 각각의 동전의 가치가 주어진다.

# 문제 풀이 : 동적 계획법으로 풀어야 한다.
import sys

dp=[0]*100000
def solution():
    global coinList, dp, K
    for coin in coinList:
        dp[coin]+=1
        for j in range(coin+1,K+1):
            dp[j]+=dp[j-coin]
    print(f'{dp[K]}')

if __name__=="__main__":
    global coinList, K
    N,K=map(int,sys.stdin.readline().split())
    coinList=[]
    for i in range(N):
        coinKind=int(sys.stdin.readline())
        if coinKind<=K:
            coinList.append(coinKind)
    solution()