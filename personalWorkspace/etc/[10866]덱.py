# 작성일자 20210202
# 문제명 : 백준 [10866] 덱
# 문제 요약 : 


import sys



def solution(inputedCommend,dack):
    if inputedCommend[0:10]=="push_front":
        number=list(map(str,inputedCommend.split()))[1]
        dack.insert(0,number)
    elif inputedCommend[0:9]=="push_back":
        number=list(map(str,inputedCommend.split()))[1]
        dack.append(number)
    elif inputedCommend[0:4]=="back":
        if not dack:
            print(-1)
        else:
            print(dack[-1])
    elif inputedCommend[0:5]=="front":
        if not dack:
            print(-1)
        else:
            print(dack[0])
    elif inputedCommend[0:4]=="size":
        print(len(dack))
    elif inputedCommend[0:5]=="empty":
        if not dack:
            print(1)
        else:
            print(0)
    elif inputedCommend[0:9]=="pop_front":
        if not dack:
            print(-1)
        else:
            print(dack.pop(0))
    elif inputedCommend[0:8]=="pop_back":
        if not dack:
            print(-1)
        else:
            print(dack.pop())


if __name__=="__main__":
    inputedCommendNum=int(sys.stdin.readline())
    dack=[]
    #print(inputedCommendNum)
    for i in range(inputedCommendNum):
        inputedCommend=sys.stdin.readline().strip()
        #print(inputedCommend)
        solution(inputedCommend,dack)