# 남은 시간 : 2시간
# 모든 경우의 수를 구하면 된다 
from itertools import permutations
from itertools import combinations_with_replacement
import numpy as np


def solution(n, info):
    answer = []
    data = [10,9,8,7,6,5,4,3,2,1,0]
    score_board = [10,9,8,7,6,5,4,3,2,1,0]
    apeach:np.array = np.array(info)
    result = list(combinations_with_replacement(data,n))
    lion_cases = []
    #print(result[0])
    for i in result:
        if sum(i)!=n:
            continue
        lion_cases.append(np.array(i))

    max_score_differnce=0
    apeach_score=0
    lion_score=0
    # 여기서 값이 같아서 0이 된 경우는 제외해줘야 한다. 그냥 np 쓰지 말까..
    for lion_case in lion_cases:
        for index,apeach_value,lion_value in enumerate(zip(apeach,lion_case)):
            if apeach_value!=0 and apeach_value==lion_value or apeach_value>lion_value:
                apeach_score+=score_board[index]
            else:
                lion_score+=score_board[index]
        score_differnce = lion_score-apeach_score
        if max_score_differnce <= score_differnce:
            max_score_differnce = score_differnce
            answer = lion_case

    return answer