# 작성일자 : 20210403
# 문제명 : 풍선 터트리기 [월간 코드 챌린지 시즌1 2번째 문제]
# 문제 풀이 
# 조건 1. 자신을 기준으로 양쪽에 자신보다 작은 값이 있으면 안된다.
# -> 한쪽에는 작은 값이 있어도 된다.
# 위 조건을 만족하는 O(N)을 찾으면 된다.
# O(N)의 시간 복잡도를 가져야 한다.
# 만약 이 값이 len(a)를 넘는다면 len(a)가 답
# 어떻게 해야 O(N)의 시간 복잡도를 가질 수 있을까?
# 일단 크기를 한번 쭉 비교를 해야한다.

def solution(a):
    answer = [ False for _ in range(len(a))]
    min_left,min_right = float("inf"),float("inf")
    for index,_ in enumerate(a):
        if a[index]<min_left:
            min_left=a[index]
            answer[index]=True
        if a[-1-index]<min_right:
            min_right=a[-1-index]
            answer[-1-index]=True
    print(sum(answer))
    return sum(answer)


if __name__=="__main__":
    a_list=[[10,7,1,2,3,4,5,6,9,8],[9,-1,-5],[-16,27,65,-2,58,-92,-71,-68,-61,-33]]
    for a in a_list:
        print('===')
        print(a)
        solution(a)
