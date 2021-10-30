'''
무한히 많은 회의실을 보유하는 회사가 고객에게 회의실을 대여해주는 서비스를 제공하고 있다.
고객은 원하는 시간대에 회의실을 예약 가능하다. 
고객은 예약한 시간 동안 반드시 사용
예약무한한 회의실을 유지하는 비용을 줄이고자 어제 하루 동안 동시에 사용 중인 회의실 수가 가장 많은 시각을
구해서 유동적으로 회의실 관리하는 중.
이전 날 회의실 사용 정보가 담긴 2차원 배열 info가 매개변수로 주어질 대,
동시에 사용 중인 회의실의 수가 가장 많았던 시각을 전부 구하여 return
'''
import numpy as np

def solution(info):

    answer:list = []
    times = np.array([0]*86399)
    for start,end in (info):
        times[start:end+1]+=1

    max_time=0
    for i,time in enumerate(times):
        if time>max_time:
            max_time=time
            answer=[i]
        elif time==max_time:
            answer.append(i)
        else:
            pass

    return answer