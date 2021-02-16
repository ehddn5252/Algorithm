# 작성일자 : 20210216
# 문제명 : 이중 우선순위 큐
# 문제 요약: 이중 우선순위 큐 구현

import heapq
from sys import stdin

if __name__=="__main__":
    testcase=int(stdin.readline())
    for _ in range(testcase):
        operatorNum=int(stdin.readline().strip())

        list1=[]
        for _ in range(operatorNum):
            operator=stdin.readline().strip()
            if operator[0]=="I":
                num=int(operator[2:])
                list1.append(num)
            elif operator=="D 1":
                if list1:
                    list1.remove(max(list1))
            elif operator=="D -1":
                if list1:
                    list1.remove(min(list1))
                

        if list1:
            print(f'{max(list1)} {min(list1)}')
        else:
            print(f'EMPTY')