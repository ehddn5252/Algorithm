# 작성일자 : 20210720
# 작성자 : 김동우
# 문제명 : 잃어버린 괄호
# 문제 요약 : 
'''
1. 세준이는 + - 괄호를 가지고 식을 만들었다. 그러고 괄호를 모두 지웠다.
2. 괄호를 적절히 쳐서 이 식의 값을 최소로 만드려고 한다.
'''

# 첫째 줄에 식이 주어진다. 식은 0-9, + -로만 이루어져 있고 가장 처음과 마지막은 숫자이다.
# 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리 보다 많이 연속되는 숫자는 없다.
# 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.


# 문제 해결 :
'''
키포인트 : 뒤에서부터 플러스끼리 먼저 계산하고 맨 마지막에 -를 계산?.
1. input_string에 넣어야 한다.
2. 
'''

from sys import stdin



def solution(input_string):
    number=''
    number_list= []
    operator_list = []
    for i in input_string:
        if i>='0' and i<='9':
            number+='i'
        else:
            number_list. append(int(number))
            operator_list.append(i)

if __name__=="__main__":
    input_string= stdin.readline().strip()
    solution(input_string)