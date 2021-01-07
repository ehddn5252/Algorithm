# 작성자 : 김동우
# 작성일자 : 20201228
# 문제명 : 2504 괄호의 값
# 문제 풀이 : 스택, 재귀
# 1. (가 나오면 2() [가 나오면 3() 으로 값을 정해준다.
# 2. )나왔을 때 만약 top에 (가 아니라면 괄호를 넣어준다.
# 모르겠으..



stack=[]
answer=1


def solution(inputedStr):
    for value in inputedStr:
        if value=="(":
            stack.append('(')
        elif value=="[":
            stack.append('[')
        elif value==")":
            if stack[-1]=="(":
                stack.pop()
            else:
                stack.append('(')
        elif value=="]":
            if stack[-1]=="[":
                stack.pop()
            else:
                stack.append(']')



if __name__ == "__main__":
    inputedStr = input()
    solution(inputedStr)

