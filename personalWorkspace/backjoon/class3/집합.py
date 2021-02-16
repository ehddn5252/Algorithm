# 작성일자 : 20210216
# 문제명 : 집합 11723
# 문제 요약: set을 구현


from sys import stdin

if __name__=="__main__":
    operatorNum=int(stdin.readline())
    fullSet=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    emptySet=set([])
    set1=set([])
    for _ in range(operatorNum):
        operator=stdin.readline().strip()
        if operator[0:3]=="add":
            set1.add(int(operator[4:]))
        elif operator[0:6]=="remove":
            if int(operator[7:]) in set1:
                set1.remove(int(operator[7:]))
        elif operator[0:5]=="check":
            if int(operator[6:]) in set1:
                print(1)
            else:
                print(0)
        elif operator[0:6]=="toggle":
            if int(operator[7:]) in set1:
                set1.remove(int(operator[7:]))
            else:
                set1.add(int(operator[7:]))
        elif operator[0:3]=="all":
            set1 = set1 | fullSet
        elif operator[0:5]=="empty":
            set1 = set1 & emptySet
            
