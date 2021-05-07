# 작성 일자 : 20210507
# 작성자 : 김동우
# 문제명 : 음양 더하기
# 문제 요약 : 정수의 절대값 모음인 absolutes와 부호의 모음인 signs를 통해 절대값 이전의 정수들의 합을 구하라 
'''
예시
absolutes	signs	result
[4,7,12]	[true,false,true]	9
''''

def solution(absolutes, signs):
    answer=0
    for index,sign in enumerate(signs):
        if sign==True:
            answer+=absolutes[index]
        else:
            answer-=absolutes[index]
    return answer