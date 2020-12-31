# 작성일자 : 20201228
# 작성자 : 김동우
# 문제 : OX 퀴즈 ( 백준 8958)
# 문제 요약 : 
# 1.OX퀴즈의 결과가 있다 O는 문제를 맞은 것 X는 문제를 틀린 것이다.
# 2. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 3. OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 문제 풀이 : 
# 말 그대로 구현, 별 생각할 건 없다.

import sys

def solution():
    strList=[]
    ansList=[]
    sumValue=0
    stack=0
    try:
        n = int(sys.stdin.readline())
        for _ in range(n):
            inputedStr = sys.stdin.readline()
            strList.append(inputedStr)
    except:
        pass
    
    for givenString in strList:
        for value in givenString:
            if value=="O":
                stack+=1
                sumValue+=stack
            elif value=="X":
                stack=0
        stack=0
        ansList.append(sumValue)
        sumValue=0

    for i in ansList:
        print(i)

if __name__ == "__main__":
    solution()