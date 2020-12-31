# 작성일자 : 20201231
# 작성자 : 김동우
# 문제명 : 그룹 단어 체커 (백준 1316)

import sys


def solve():
    n= int(sys.stdin.readline())
    ans=0
    for _ in range(n):
        string=input()
        stringDic={}
        addFlag=1
        for index,value in enumerate(string):
            if value not in stringDic.keys():
                stringDic[value]=1
            elif value in stringDic.keys() and value!=string[index-1]:
                addFlag=0
        ans+=addFlag
    print(ans)


if __name__ == "__main__":
    solve()