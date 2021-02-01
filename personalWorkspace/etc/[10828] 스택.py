# 작성일자 20210201
# 문제명 : 백준 [10828] 스택
# 문제 풀이 : 
# 스택 명령어를 직접 구현한다.
import sys

def solution(inputedCommend,stack):
    if inputedCommend[0:4]=="push":
        number=list(map(str,inputedCommend.split()))[1]
        stack.append(number)
    elif inputedCommend[0:3]=="top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif inputedCommend[0:4]=="size":
        print(len(stack))
    elif inputedCommend[0:5]=="empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif inputedCommend[0:3]=="pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())


if __name__=="__main__":
    inputedCommendNum=int(sys.stdin.readline())
    stack=[]
    #print(inputedCommendNum)
    for i in range(inputedCommendNum):
        inputedCommend=sys.stdin.readline().strip()
        #print(inputedCommend)
        solution(inputedCommend,stack)