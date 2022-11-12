from itertools import permutations
from itertools import product
def solution(k):

    d:dict = {0:6, 1:2, 2:5, 3:5, 4:4,5:5,6:6,7:3,8:7,9:6}
    sets_num = [6,2,5,5,4,5,6,3,7,6]
    sets = [0,1,2,3,4,5,6,7,8,9]
    # 순열 사용해서 다 돌려보기
    count=0
    for i in product(sets, repeat = 1):
        sum_value=0
        if i[0]==0:
            continue
        for j in range(len(i)):
            sum_value+=d[i[j]]
        if sum_value==k:
            count+=1

    for i in product(sets, repeat = 2):
        sum_value=0
        if 10>int(str(i[0])+str(i[1])):
            continue
        for j in range(len(i)):
            sum_value+=d[i[j]]
        if sum_value==k:
            count+=1

    for i in product(sets, repeat = 3):
        sum_value=0
        if 100>int(str(i[0])+str(i[1])+str(i[2])):
            continue
        for j in range(len(i)):
            sum_value+=d[i[j]]
        if sum_value==k:
            count+=1

    for i in product(sets, repeat = 4):
        sum_value=0
        if 1000>int(str(i[0])+str(i[1])+str(i[2])+str(i[3])):
            continue
        for j in range(len(i)):
            sum_value+=d[i[j]]
        if sum_value==k:
            count+=1
    for i in product(sets, repeat = 5):
        sum_value=0
        if 10000>int(str(i[0])+str(i[1])+str(i[2])+str(i[3])+str(i[4])):
            continue
        for j in range(len(i)):
            sum_value+=d[i[j]]
        if sum_value==k:
            count+=1

    for i in product(sets, repeat = 6):
        sum_value=0
        if 100000>int(str(i[0])+str(i[1])+str(i[2])+str(i[3])+str(i[4])+str(i[5])):
            continue
        for j in range(len(i)):
            sum_value+=d[i[j]]
        if sum_value==k:
            count+=1


    return count