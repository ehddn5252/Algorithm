# 작성일 : 20210124
# 작성자 : 김동우 
# 문제 요약 : 피보나치 : 0 1 1 2 3 5 8 13 21 34 55 89 144 ...
# 각 테스트 케이스마다 fibonacci(0)이 출력되는 횟수와 fibonacci(1)이 출력되는 횟수를 공백으로 구분해서 출력 
# 문제 풀이 : 
#  1. 리스트를 만들어서 안에 fibonacci(0)의 횟수와 fibonacci(1)의 횟수를 저장해 놓는다.
#  2. 이를 기준으로 DP를 만들어 놓는다.
#  3. 초기 조건은 0일때 [1,0] 1일때 [0,1]  2일때 [1,0]+ [0,1] = [1,1] 3일때 [1,0] + [1,1] = [2,1] 이고
#  4. 점화식은 dp[i][0] = dp[i-1][0] + dp[i-2][0]
#  5. dp[i][1] = dp[i-1][1] + dp[i-2][1] 로 dp 배열을 만든다.
# 

'''
def fibonacci(n):
    if n==0:
        print(0)
        return 0
    elif n==1:
        print(1)
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
'''

def solution(N,dp):
    # dp초기화
    for i in range(N-2):
        dp.append([0,0])
    # dp 배열 생성
    for i in range(2,N+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    
    print(str(dp[N][0])+" "+str(dp[N][1]))

if __name__=="__main__":
    testcase=int(input())
    dp=[[1,0],[0,1],[1,1]]
    
    for i in range(testcase):
        N=int(input())
        solution(N,dp[:])

