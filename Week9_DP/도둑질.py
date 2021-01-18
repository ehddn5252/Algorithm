# 문제 풀이
# 맨 첫번째 집을 털 지 안털지 확인해야 한다.
# 맨 첫번째를 턴다면 2번째를 안턴다.
# 지금 money+ 2번전꺼와 1번전꺼를 비교만 하면 된다.

def solution(money):
    answer = []
    dp = [0 for _ in range(len(money))]
    # 첫번째 집 선택 여기서 dp[1]를 money[0]으로 초기화 하지 않으면 하나가 틀리는데 뭔 경우일까
    dp[0]=dp[1]=money[0]
    for i in range(2,len(money)):
        dp[i]= max(dp[i-1],dp[i-2]+money[i])
    answer.append(dp[-2])

    # 두번째 집 선택
    dp = [0 for _ in range(len(money))]
    dp[1]=money[1]
    for i in range(2,len(money)):
        dp[i]=max(dp[i-1],dp[i-2]+money[i])
    answer.append(dp[-1])

    # 첫번째, 두번째 둘 다 선택x
    dp = [0 for _ in range(len(money))]
    for i in range(2,len(money)):
        dp[i]=max(dp[i-1],dp[i-2]+money[i])
    answer.append(dp[-1])
    print(max(answer))
    return max(answer)

if __name__ == "__main__":
    solution([1,2,3,1])