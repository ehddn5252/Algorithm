# 작성일자 : 20210202
# 문제명 : 큰 수의 법칙
# 문제 요약 :
# 1. 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M(maxSumTimes)번 더하여 가장 큰 수를 만드는 법칙
# 2. 배열의 특정한 인덱스에 해당하는 수가 연속해서 K(noMorethanNumber)번을 초과하여 더해질 수 없다
# 입력 으로는 배열의 길이 N M K 가 첫줄에 주어지고 두번째 줄에는 수들이 주어진다.
# 문제 풀이 :
# 수학적으로도 풀 수 있다.
import sys

def solution(numList,maxSumTimes,noMorethanNumber):
    numList.sort(reverse=True)
    maxNumber=numList[0]
    secondMaxNumber=numList[1]
    answer=((maxSumTimes//(noMorethanNumber+1))*noMorethanNumber+(maxSumTimes%(noMorethanNumber+1)))*maxNumber
    answer+=(maxSumTimes//(noMorethanNumber+1))*secondMaxNumber
    print(answer)
    
if __name__=="__main__":
    _,maxSumTimes,noMorethanNumber= map(int,sys.stdin.readline().split())
    numList=list(map(int,sys.stdin.readline().split()))
    solution(numList,maxSumTimes,noMorethanNumber)

    