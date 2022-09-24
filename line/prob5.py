from typing import List


def solution(fees: List[List[int]], t: int) -> List[int]:
    '''
    각 차량들이 주차한 시간과 부과한 요금이 주어졌을 때, 요금을 예측하라
    '''
    answer = []
    fees.sort(key=lambda x: x[0])
    min_dp = [0 for _ in range(fees[-1][0]+1)]
    max_dp = [0 for _ in range(fees[-1][0]+1)]

    print(fees)
    '''
    dp 로 생각
    시간 텀을 계산해야 한다.
    1. 시간대별로 정렬
    2. 
    '''
    before = 0
    for fee in fees:
        min_dp[fee[0]] = fee[1]
    print(min_dp)
    return answer


fees = [[4, 1000], [6, 1000], [21, 3000], [16, 2000], [26, 3000]]
t = 2

solution(fees, t)
