# 작성일자 : 20201230
# 작성자 : 김동우
# 문제명 : 아스키 코드
# 문제 요약 : 문자 아스키 코드로 변환

import sys


def solve():
    inputedValue=sys.stdin.readline()
    print(ord(inputedValue[0]))


if __name__ == "__main__":
    solve()