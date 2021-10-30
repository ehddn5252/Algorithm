'''
문제 요약:
트럭들이 일렬로 고속도로 운행한다.
첫 번째 트럭의 연료는 많이 사용되지만 그 다음 트럭들은 공기 저항을 덜 받아서 연료 사용량이 줄어든다.
여러 대의 트럭이 군집 주행을 할때 연료를 절약하기 위해 선 트럭을 교체한다.

각 트럭이 처음에 가지고 있는 연료량이 담긴 배열 v,
선두 트럭의 시간당 연료 소비량 a, 후위 트럭의 시간당
연료 소비량 b가 주어진다. 
선두 트럭 교체 방식을 썼을 때 최대 몇 시간 운행 가능한 지 return 하도록 함수 완성하기 
어느 트럭이라도 1시간 동안 운행할 연료량이 되지 않으면 운행을 종료한다.
'''
"""
문제 풀이:
연료가 최대로 남은 트럭을 맨 앞과 바꿔준다.
계산식을 사용하면 더 빠르게 할 수 있을 것 같다.
맨 앞에 있는 트럭만 a 사라지고, 나머지 트럭은 b씩 사라진다.
 O(N^2) 으로 풀면 안된다
"""
import numpy as np

def solution(v, a, b):
    answer=0
    v=np.array(v)
    min_value = min(v[1:])
    least=100000
    while v[0]>=a and min_value>=b:
        v = v-b
        v[0]=v[0]-a + b
        for index, value in enumerate(v):
            if value<min_value:
                min_value = value
            if value > v[0]:
                tmp = value
                v[index] = v[0]
                v[0]=tmp
        answer+=1

    return answer