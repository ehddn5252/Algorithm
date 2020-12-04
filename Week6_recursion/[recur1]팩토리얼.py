# 작성일자 : 20201204
# 작성자 : 김동우
# 문제명 : 10872 팩토리얼
# 문제 풀이 : N이 입력으로 주어질 때 N!을 출력하라
# 문제 해석 :
# 1. num이 1보다 클 때는 num* recur(num-1)
# 2. 아니면 1을 return한다
 
def recur(num):
    if num>1:
        return num*recur(num-1)
    else: 
        return 1

def solution():
    N=int(input())
    ans=recur(N)
    print(ans)


if __name__ == "__main__":
    solution()