# 작성일자 20210201
# 문제명 : 백준 [9012] 괄호
# 
import sys

def solution(inputedBrackets):
    stack=[-1]
    for bracket in inputedBrackets:
        if bracket=='(':
            stack.append(1)
        elif bracket==')':
            if not stack:
                break
            stack.pop()
    if not stack:
        print("NO")
    elif stack[-1]==-1:
        print("YES")
    else:
        print("NO")



if __name__=="__main__":
    testCase=int(sys.stdin.readline())
    for i in range(testCase):
        inputedBrackets=sys.stdin.readline().strip()
        solution(inputedBrackets)