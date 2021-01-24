# 문제 요약
# 정수 X에 할 수 있는 연산은 3가지가 있다.
# 1. X가 3으로 나누어 떨어지면 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면 2로 나눈다.
# 3. 1을 뺀다
# 위 연산 3가지를 적절히 섞어 1로 만들 때 연산을 사용하는 횟수의 최솟값을 출력하라.   

# DP는 초기 조건, DP 배열, 점화식으로 이루어진다.

def solution(N):
    answer=0
    dp=[[N]]
    # 예외
    if N==1:
        print(0)
        return 
    for _ in range(40):
        dp.append([])
    while True:
        for n in dp[answer]:
            tmp =n-1
            dp[answer+1].append(tmp)

            if n%2==0 and n>>1 not in dp[answer]:
                tmp=n>>1
                dp[answer+1].append(tmp)
            if n%3==0 and n//3 not in dp[answer]:
                tmp=n//3
                dp[answer+1].append(tmp)
            if 1 in dp[answer+1]:
                print(answer+1)
                return
            setedDP=set(dp[answer+1])
            dp[answer+1]=list(setedDP)
        answer+=1



if __name__ == "__main__":
    N=int(input())
    solution(N)
