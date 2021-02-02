# 참고 : https://claude-u.tistory.com/208

# 작성일자 : 20210124
# 문제 요약 : 첫줄에 물품의 수 (N)와 배낭의 무게(K)가 주어지고 
# 그 다음부턴 물건의 무게와 가치가 주어진다.
# 물건의 무게 합이 배낭의 무게를 넘지 않을 때 배낭에 가장 큰 가치를
# 출력하시오 
# 알고리즘 생각 : DFS쓰면 시간초과 난다. -> DP로 하자.
# 초기조건, DP배열, 점화식
# 초기 조건 : 맨 처음에 어떤 것을 넣든 순서는 상관이 없다.
# 맨 처음 시작하는 것을 다르게 하면서 모든 경우의 수를 확인한다. 


def solution():
    goodsNum,maxWeight=list(map(int,input().split()))
    # 맨 처음에 0,0에서 더해가는 식이다
    weightAndValue=[[0,0]]
    for _ in range(goodsNum):
        weightAndValue.append(list(map(int,input().split()))) 
    # K행 N열을 가지는 리스트 생성
    dp= [[0 for _ in range(maxWeight+1)] for _ in range(goodsNum+1)]

    for order in range(goodsNum+1):
        for currentWeight in range(maxWeight+1):
            weight=weightAndValue[order][0]
            value=weightAndValue[order][1]
            # 만약 무게를 초과한다면 이전 값을 가져온다
            if weight>currentWeight:
                dp[order][currentWeight]=dp[order-1][currentWeight]
            # 무게를 초과하지 않는다면 이전 값과 이전 값에 지금 value를 더한 값과 비교해서 더 큰 값을 저장한다.
            else:
                dp[order][currentWeight]=max(dp[order-1][currentWeight-weight]+value,dp[order-1][currentWeight])

    print(dp[goodsNum][maxWeight])


if __name__ =="__main__":
    solution()
