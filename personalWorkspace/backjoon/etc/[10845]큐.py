# 작성일자 20210202
# 문제명 : 백준 [10845] 큐
# 문제 요약 : 


import sys



def solution(inputedCommend,queue):
    if inputedCommend[0:4]=="push":
        number=list(map(str,inputedCommend.split()))[1]
        queue.append(number)
    elif inputedCommend[0:4]=="back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    elif inputedCommend[0:5]=="front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif inputedCommend[0:4]=="size":
        print(len(queue))
    elif inputedCommend[0:5]=="empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif inputedCommend[0:3]=="pop":
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))


if __name__=="__main__":
    inputedCommendNum=int(sys.stdin.readline())
    queue=[]
    #print(inputedCommendNum)
    for i in range(inputedCommendNum):
        inputedCommend=sys.stdin.readline().strip()
        #print(inputedCommend)
        solution(inputedCommend,queue)