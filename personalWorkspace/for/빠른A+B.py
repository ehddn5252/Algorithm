# 작성일 : 20201228
# 작성자 : 김동우
# 문제명 : 빠른 A+B
# 문제 요약 : 문제에 나오는 a+b를 출력 다만 언제 종료될 지 모른다.

# 문제 풀이 : try except문을 사용하면 에러시 자동으로 종료된다.

import sys

def solution():
    while 1:
        try :
            tmpA,tmpB = map(int,sys.stdin.readline().split())
            print(tmpA+tmpB)
        except:
            break

if __name__ == "__main__":
    solution()
