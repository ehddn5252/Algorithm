from typing import List, Dict


def check_double(num):
    double = 1
    while True:
        if double >= num:
            return double
        else:
            double *= 2


def solution(queries: List[List[int]]) -> int:
    '''
    1. 바구니에 따른 딕셔너리 만든다.
    2. 2의 배수 확인
    3.
    '''
    ans = 0
    dict1: Dict = {}
    # {{1}: [now
    for i in range(len(queries)):
        if queries[i][0] not in dict1.keys():
            dict1[queries[i][0]] = [queries[i][1], check_double(queries[i][1])]

        else:
            new_num = queries[i][1]+ dict1[queries[i][0]][0]
            if new_num > dict1[queries[i][0]][1]:
                ans += dict1[queries[i][0]][0]
            dict1[queries[i][0]] = [new_num, check_double(new_num)]
    return ans


queries = [[2,10],[7,1],[2,5],[2,9],[7,32]]
print(solution(queries))