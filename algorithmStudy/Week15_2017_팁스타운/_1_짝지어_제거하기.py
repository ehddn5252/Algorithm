# 작성일자 : 20210227
# 문제명 : 짝지어 제거하기
# 문제 요약 : 문자열이 있다. 이 문자열에서 짝지어 있는 알파벳 2개를 찾고 그 둘을 제거하고
# 앞 뒤로 문자열을 이어 붙인다. 문자열을 모두 제거한다면 짝지어 제거하는 거이 종료된다.
# 짝지어 제거하는 것을 모두 성공적으로 수행할 수 있다면 1 아니면 0을 리턴하시오
# 문자열의 길이가 1,000,000 이라서 1번만에 통과할 수 있어야 한다.
# 문제 풀이 :
# 1. 처음부터 스택과 비교한다.
# 2. 만약 스택 top에 존재하면 top을 pop한다.
# 3. 아니면 stack에 넣는다.
# 4. 만약 stack이 empty면 1 아니면 0을 반환한다.

def solution(string):
    stack1=[]
    for _,value in enumerate(string):
        if stack1 and stack1[-1]==value:
            stack1.pop()
        else:
            stack1.append(value)
    if not stack1:
        return 1
    else:
        return 0

