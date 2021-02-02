# 작성일자 20210201
# 문제명 : 백준 [2475] 검증수

import sys
def solution(numberList):
    sumValue=0
    for number in numberList:
        sumValue+=number**2
    print(sumValue%10)




if __name__=="__main__":
    numberList=list(map(int,sys.stdin.readline().split()))
    solution(numberList)