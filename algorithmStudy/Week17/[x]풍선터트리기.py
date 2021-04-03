# 작성일자 : 20210403
# 문제명 : 풍선 터트리기 [월간 코드 챌린지 시즌1 2번째 문제]
# 문제 풀이 
# 조건 1. 자신을 기준으로 양쪽에 자신보다 작은 값이 있으면 안된다.
# 위 조건을 만족하는 O(N)을 찾으면 된다.
# O(N)의 시간 복잡도를 가져야 한다.
# -> 양 끝이 몇 번째로 큰 수인지 확인한다.
# -> max(왼쪽 끝 순위, 오른쪽 끝 순위)가 값이 답이다.
# 만약 이 값이 len(a)를 넘는다면 len(a)가 답



def solution(a):
    answer = 0

    left_rank=1
    right_rank=1
    for value1 in a:
        if a[-1]>value1:
            right_rank+=1
        if a[0]>value1:
            left_rank+=1 
    print(f'left_rank,right_rank : {left_rank} , {right_rank}')
    answer=max(right_rank,left_rank)
    print(f'answer : {answer}')
    return answer


if __name__=="__main__":
    a_list=[[10,7,1,2,3,4,5,6,9,8],[9,-1,-5],[-16,27,65,-2,58,-92,-71,-68,-61,-33]]
    for a in a_list:
        print('===')
        print(a)
        solution(a)