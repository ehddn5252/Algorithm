# 작성일자 : 20210403
# 문제명 : 풍선 터트리기 [월간 코드 챌린지 시즌1 2번째 문제]
# 문제 풀이 
# 조건 1. 자신을 기준으로 양쪽에 자신보다 작은 값이 있으면 안된다.
# 위 조건을 만족하는 O(N)을 찾으면 된다.
# O(N)의 시간 복잡도를 가져야 한다.




def solution(a):
    answer = 0
    answer=len(a)
    for index1,value1 in enumerate(a):
        left_check=False
        right_check=False
        for index2,value2 in enumerate(a):
            if index1>index2 and value1>value2:
                left_check=True
            if index1<index2 and value1>value2:
                right_check=True
            if left_check==True and right_check==True:
                answer-=1
                break
    return answer