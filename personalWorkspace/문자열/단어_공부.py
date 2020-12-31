# 작성일자 : 20201231
# 작성자 : 김동우
# 문제명 : 단어 공부
# 문제 요약 : 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 문제 풀이 : 문자열을 대문자로 바꾼다
# alpabetDic에 알파벳을 넣고 문자열을 탐색한다.
# maxValue가 2개 이상이면 ? 아니면 그 알파벳을  

import sys


def solve():
    n=sys.stdin.readline()
    upperN=n.upper()
    finalN=upperN[0:-1]
    alpabetDic={}
    for i in finalN:
        if i not in alpabetDic.keys():
            alpabetDic[i]=1
        else:
            alpabetDic[i]+=1
    maxValue=0
    for key,value in alpabetDic.items():
        if value>maxValue:
            ans=key
            maxValue=value
        elif value==maxValue:
            ans='?'
    print(ans)

if __name__ == "__main__":
    solve()