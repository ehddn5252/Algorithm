# 작성일자 : 20210202
# 문제명 : 1이 될 때 까지
# 문제 요약 : 어떠한 수 N이 1이 될 때까지 아래 두가지 과정 중 하나를 반복적으로 선택하여 수행할 수 있다.
# 단 두번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다. 
# 2. N을 K로 나눈다.
# 문제 풀이 : 나누어 떨어진다면 나누고 안 나누어 떨어진다면 modular 연산을 한 값을 N에서 뺀다.
# 이를 N이 0이 될 때까지 반복하는데, 0이 되는 경우는 1에서 1을 뺀 경우이다
# 그러므로 맨 마지막 answer에 1을 더해주면 1이 되는 수가 된다. 
import sys

def solution(N,dividingNumber):
    answer=0
    while N>0:
        if N%dividingNumber==0:
            answer+=1
            N//=dividingNumber
        else:
            answer+=N%dividingNumber
            N-=N%dividingNumber
    print(answer-1)

if __name__=="__main__":
    N,dividingNumber= map(int,sys.stdin.readline().split())
    solution(N,dividingNumber)

    