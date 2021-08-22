# 작성일자 : 20210727
# 작성자 : 김동우
# 문제명 : four squares
# 문제 요약 : 
# 1. 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현가능하다.
# 2. 자연수가 주어질 때 최소 개수의 제곱수 합으로 표현하고 그 개수를 출력하라. 

# 알고리즘 :
# 가장 큰 숫자부터 차례로 고른다. 
# 그 다음으로 큰 숫자를 고른다.
# 1 : 1 2: 1+1 3:1+1+1 4 : 2^^2 5 : 2**2 + 1**1 6 : 2**2 + 1 + 1 7: 8 : 

import math

N = int(input())
dp = [0 for _ in range(0,50001)]

dp[0]=1
dp[1]=1
dp[2]=2


for index in range(N+1):
    sqrt_value = int(math.sqrt(index))
    if sqrt_value**2 == index:
        dp[index] = 1
    else:
        three_times = 4
        if math.pow(math.sqrt(index//3),2)*3==index:
            three_times = 3
        dp[index] = min( 1 + dp[index-sqrt_value**2], dp[index-1]+1,three_times)

print(dp[N])


a