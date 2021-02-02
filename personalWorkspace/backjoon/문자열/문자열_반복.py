# 작성일자 : 20201231
# 작성자 : 김동우
# 문제명 : 문자열 반복 (백준 2675)
# 문제 요약 : 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

import sys


def solve():
    n=int(sys.stdin.readline())
    ansList=[]
    for _ in range(n):
        givenStr=input()
        times=int(givenStr[0])
        ansStr=""
        editedGivenStr=givenStr[2:]
        for i in editedGivenStr:
            for _ in range(times):
                ansStr+=i
        print(ansStr)

if __name__ == "__main__":
    solve()