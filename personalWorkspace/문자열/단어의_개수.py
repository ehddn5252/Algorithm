# 작성일자 : 20201231
# 작성자 : 김동우
# 문제명 : 단어의 개수 (백준 1152)
# 문제 요약 : 영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다.
# 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.
# 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

# 문제 풀이 : strip으로 양쪽 공백을 제거하고 띄어쓰기 개수를 구한다.

import sys


'''
def solve():
    try:
        n=sys.stdin.readline()
        n=n.strip()
        ans=1
        for i in n:
            if i is ' ':
                ans+=1
        print(ans)
    except:
        print(0)
'''

def solve():
    n=list(sys.stdin.readline().split())
    print(len(n))
if __name__ == "__main__":
    solve()