# 작성일자 : 20201230
# 작성자 : 김동우
# 문제명 : 알파벳 찾기
# 문제 요약 : 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

import sys


def solve():
    inputedString=sys.stdin.readline()
    alpabetList=[]
    for _ in range(26):
        alpabetList.append(-1)
    inputedString=inputedString[0:-1]
    for index,value in enumerate(inputedString):
        compare=ord(value)-97
        if alpabetList[compare]==-1:
            alpabetList[compare]=index

    ansString=""
    for index,value in enumerate(alpabetList):
        if index!=-1:
            ansString+=str(value)+" "
    print(ansString)

if __name__ == "__main__":
    solve()