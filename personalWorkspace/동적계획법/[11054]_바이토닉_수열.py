import sys

# 문제명 : 백준 11054 가장 긴 바이토닉 부분 수열
# 작성 일자 : 20210201
# 문제 요약 : 가장 긴 바이토닉 부분 수열을 찾는 것이다.
# 가장 큰 
'''
문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.
'''

def solution(numberList):

    dpUp=[1]*len(numberList)
    for i in range(len(numberList)):
        for j in range(i):
            if numberList[j]<numberList[i]:
                dpUp[i]=max(dpUp[j]+1,dpUp[i])
    
    reveredNumberList=numberList[:]
    reveredNumberList.reverse()
    dpDown=[1]*len(reveredNumberList)
    for i in range(len(reveredNumberList)):
        for j in range(i):
            if reveredNumberList[j]<reveredNumberList[i]:
                dpDown[i]=max(dpDown[j]+1,dpDown[i])
    dpDown.reverse()

    dp=[0]*len(numberList)
    for i in range(len(dp)):
        dp[i]=dpDown[i]+dpUp[i]-1
    
    print(max(dp))

if __name__=="__main__":
    N= int(sys.stdin.readline())
    numberList=list(map(int,sys.stdin.readline().strip().split()))
    solution(numberList)