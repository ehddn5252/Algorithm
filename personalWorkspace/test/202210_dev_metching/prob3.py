from itertools import permutations
from itertools import product
def solution(k):

    d:dict = {0:6, 1:2, 2:5, 3:5, 4:4,5:5,6:6,7:3,8:7,9:6}
    sets_num = [6,2,5,5,4,5,6,3,7,6]
    sets = [0,1,2,3,4,5,6,7,8,9]
    # 순열 사용해서 다 돌려보기
    count=0
    for i in product(sets, repeat = 1):
        if(sum(i))==k:
            count+=1

    for i in product(sets, repeat = 2):
        if(sum(i))==k:
            count+=1

    for i in product(sets, repeat = 3):
        if i[0]==0:
            continue
        if(sum(i))==k:
            count+=1
    for i in product(sets, repeat = 4):
        if(sum(i))==k:
            count+=1
    for i in product(sets, repeat = 5):
        if(sum(i))==k:
            count+=1

    for i in product(sets, repeat = 7):
        if(sum(i))==k:
            count+=1



    return count