# 작성일 : 20210722 
# 작성자 : 김동우
# 문제요약 :
'''
왼쪽과 오른쪽에 점이 각각 N,M(N<M)개 있다.
중앙을 기준으로 왼쪽과 오른쪽 점을 이어 N개의 선을 그을 때 점이 cross되지 않게
하는 경우의 수를 구하시오.

'''

'''
음.. 예를
왼쪽이 3개 오른쪽이 5개라고 생각해보자.

2,2 : 1
2, 3 : 2 + F(2,2) = 3 
2, 4 : 3 + 2 + 1 = 6 = 3 + (2,3)
2,5 : 4 + F(2,4)

3,3 : 1
3,4 : 1 + 1 + 1 + 1 = 4
(3,5) : 
3 + 2 + 1 = 6
(3,6) : 4 + 3 + 2 + 1 + 3 + 2 + 1 + 2 + 1 + 1
3, 7 : 

4,4 : 1
4,5 : 5 : 5C4
4, 6 : 
'''

from itertools import combinations
dp= [[0]*30 for _ in range(30)]
#print(dp)
row = len(dp)
col = len(dp[0])

def combination_num(n,r):
    upper = 1
    under = 1
    for i in range(n-r+1,n+1):
        upper*=i
        # 5-4+1 = upper = 3*4*5
    for i in range(1,r+1):
        under*=i
    return upper/under


for i in range(row):
    for j in range(i,col):
        if i>j :
            continue
        dp[i][j] = int(dp[i][j-1] +combination_num(j,i))

T = int(input())
for i in range(T):
    N,M = map( int, input().split() )
    print(dp[N-1][M-1])
