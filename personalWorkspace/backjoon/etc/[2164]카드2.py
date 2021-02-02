# 작성일자 20210201
# 문제명 : 백준 [2164] 카드2
# 하라는 대로 구현하면 시간초과 난다.
# 그래서 시간초과가 나지 않으려면 규칙을 찾으면 되는데 규칙은 1 2 2 4 2 4 6 8 2 4 6 8 10 12 14 16 2 4 6 8 ... 로
# 2의 N승일 때의 값이 2^n이고 다시 2부터 시작해서 2씩 더해간다. dp[4]=4 dp[5]=2 dp[16]=16 dp[17]=2 dp[18]=4 ..dp[32]=32 dp[33]=2 ..이런 식으로

import sys

def solution(n):

    dp=[1]*500001
    dp[0]=0
    additiveValue=2
    squaredValue=1
    for i in range(2,500001):
        if i==2**squaredValue:
            dp[i]=i
            additiveValue=2
            squaredValue+=1
        else:
            dp[i]=additiveValue
            additiveValue=2+additiveValue
    print(dp[n])

if __name__=="__main__":
    
    n=int(sys.stdin.readline())
    solution(n)