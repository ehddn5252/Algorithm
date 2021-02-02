import sys

# 작성 일자 : 20210201
# 문제명 : 백준 11053 가장 긴 증가하는 부분 수열
# 문제 요약 : 가장 긴 증가하는 부분 수열을 찾는 것이다.
# 가장 큰 
'''
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
'''


def solution(numberList):
    dp=[1]*len(numberList)

    for i in range(len(numberList)):
        for j in range(i):
            if numberList[j]<numberList[i]:
                dp[i]=max(dp[j]+1,dp[i])
    print(max(dp))

if __name__=="__main__":
    N= int(sys.stdin.readline())
    numberList=list(map(int,sys.stdin.readline().strip().split()))

    solution(numberList)