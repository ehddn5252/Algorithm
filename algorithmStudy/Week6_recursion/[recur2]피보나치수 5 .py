# 작성일자 : 20201204
# 작성자 : 김동우
# 문제명 : 피보나치수 5
# 문제 풀이 : N이 입력으로 주어질 때 N번째 피보나치 수를 출력하라
# 문제 해석 :
# 1. 첫번째는 0이다.
# 2. 아니면 이전 수 + 현재수
 
def recur(num):
    if num==0:
        return 0
    elif(num==1):
        return 1
    else:
        return recur(num-1)+recur(num-2)
    
def solution():
    num=int(input())
    ans=recur(num)
    print(ans)

if __name__ == "__main__":
    solution()

