# 작성일자 : 20210202
# 문제명 : 큰 수의 법칙
# 문제 요약 :
# 1. 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M(maxSumTimes)번 더하여 가장 큰 수를 만드는 법칙
# 2. 배열의 특정한 인덱스에 해당하는 수가 연속해서 K(noMorethanNumber)번을 초과하여 더해질 수 없다
# 입력 으로는 배열의 길이 N M K 가 첫줄에 주어지고 두번째 줄에는 수들이 주어진다.
# 문제 풀이 :
# 1. 제일 큰 수(numList[0])와 두번째로 큰 수(numList[1])와 현재 몇번 반복했는 지(times)를 본다.
# 2. 만약 noMorethanNumber 보다 현재 반복 횟수(times)가 적으면 답에 가장 큰 수를 더하고 times를 +1한다.
# 3. answer에 더할때 마다 masSumTimes는 1씩 줄어든다.(for문을 사용하면 다른 방식으로 해도 됐지만 while문을 사용했다.)
# 4. 현재 횟수와 noMorethanNumber와 같아지면 times를 0으로 초기화하고 두번째로 큰 수를 answer에 더한다.
#  
import sys

def solution(numList,maxSumTimes,noMorethanNumber):
    numList.sort(reverse=True)
    times=0
    answer=0
    while maxSumTimes>0:
        if noMorethanNumber>times:
            times+=1
            answer+=numList[0]
        elif noMorethanNumber==times:
            times=0
            answer+=numList[1]
        maxSumTimes-=1
    print(answer)

if __name__=="__main__":
    _,maxSumTimes,noMorethanNumber= map(int,sys.stdin.readline().split())
    numList=list(map(int,sys.stdin.readline().split()))
    solution(numList,maxSumTimes,noMorethanNumber)

    
# 수학적으로 O(1)의 시간으로 풀 수 있다.
'''
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
'''
