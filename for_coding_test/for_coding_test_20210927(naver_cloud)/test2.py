'''
빌딩을 청소하는 아르바이트를 한다. 빌딩은 2차원 행렬로 표현하며, 행렬의 각 칸은 창문을 나타낸다. 
또, 각 칸에 적힌 숫자는 창문 별로 청소했을 때 지급받는 비용이다.
청소할 필요가 없어 비용을 받지 못하는 것은 0이다.

곤돌라를 타고 건물 좌측 상단에서 출발하여 창문을 닦으면서 지상까지 내려올 때
한 번에 벌 수 있는 최대 이익을 구하시오

DP를 사용하면 바로 풀 수 있다.
'''

import copy
def solution(costs,xcost,ycost):
    answer= -1
    dp_list:list = copy.deepcopy(costs)
    for row in range(len(costs)):
        for col in range(len(costs[0])):
            if col==0 and row==0:
                continue
            
            dp_list[row][col]=max(dp_list[row-1][col]+dp_list[row][col]-xcost,dp_list[row][col-1]+dp_list[row][col]-ycost)
    answer=max(dp_list[len(costs)-1])
    return answer


