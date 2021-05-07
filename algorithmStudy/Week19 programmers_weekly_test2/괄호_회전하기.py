# 작성 일자 : 20210507
# 작성자 : 김동우
# 문제명 : 괄호 회전하기
# 문제 요약 : 괄호로 이루어진 문자열 s가 있고 x칸 만큼 x<len(s) 이를 한칸씩 이동시킬 수 있다.
# x만큼 이동시켰을 때 제대로된 괄호를 만들 때 그 값을 출력하라
import copy

def solution(s):
    answer = 0
    len_s=len(s)
    for _ in range(len_s):
        copyed_s=copy.deepcopy(s)
        stack=[]
        flag=True
        for _,value in enumerate(copyed_s):
            if value == '(':
                stack.append(')')
            elif value == '{':
                stack.append('}')
            elif value =='[':
                stack.append(']')
            else:
                if not stack:
                    flag=False
                    break
                if value!=stack[-1]:
                    flag=False
                    break
                else:
                    stack.pop()

        if not stack and flag:
            answer+=1
        tmp=copyed_s[1:]
        tmp+=copyed_s[0]
        s=tmp
    return answer


