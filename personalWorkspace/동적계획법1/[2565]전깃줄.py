# 작성일자 : 20210201
# 문제명 : 백준 2565 전깃줄
# 문제 풀이 :
# 1. 가만히 생각해보면 증가하는 부분 수열과 말만 다를 뿐 로직은 같다. 증가하는 부분 수열을 그대로 사용하면 된다.
# 2. 여기에서 제거해야할 전선 수이므로 전체에서 max(dp)를 빼준다 
import sys

def solution(numberList):
    numberList.sort(key=lambda x:x[0])
    dp=[1]*len(numberList)
    for i in range(len(numberList)):
        for j in range(i):
            if numberList[i][1]>numberList[j][1]:
                dp[i]=max(dp[i],dp[j]+1)
    
    print(len(numberList)-max(dp))



if __name__=="__main__":
    N= int(sys.stdin.readline().strip())
    numberList=[]
    
    for i in range(N):
        numberList.append(list(map(int,sys.stdin.readline().split())))
    solution(numberList)