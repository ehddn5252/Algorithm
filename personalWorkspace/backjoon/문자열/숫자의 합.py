# 작성일자 : 20201230
# 작성자 : 김동우
# 문제명 : 숫자의 합
# 문제 요약 : string으로 되어있는 한자리 숫자를 모두 합해서 출력하시오
import sys


def solve():
    _=sys.stdin.readline()
    inputedValue=sys.stdin.readline()
    ans=0
    for i in inputedValue:
        if i=="\n":
            break
        ans+=int(i)
    print(ans)


if __name__ == "__main__":
    solve()