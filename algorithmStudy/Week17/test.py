# 작성일자 : 20210402
# 문제명 : 삼각 달팽이 [월간 코드 챌린지 시즌1 2번째 문제]
# 문제 풀이 
# 
# 1. 삼각형 모양 배열을 만들고 list_2d[i][j]
# 2. 방향을 정한다.
# 2-1. 방향을 아래쪽으로 설정 i값 증가 
# 만약 맨 아래 끝까지 갔거나 값이 0이 아니라면
# 2-2. 방향을 오른쪽으로 설정 j값 증가
# 오른쪽값이 끝까지 갔거나 0 값이 0이 아니면
# 2-3. 방향을 위로 설정i값,j값 감소
# 2-4. 방향을 왼쪽으로 설정 j값 감소
# 3. 종료조건을 숫자로 생각 

def sum_num(n):
    sum_value=0
    for i in range(1,n+1):
        sum_value+=i
    return sum_value

def solution(n):
    answer = []
    count_number=1
    reach_number=sum_num(n)
    list_2d = [[0]*i for i in range(1,n+1)]
    down=0
    right=1
    up=2
    left=3
    direction=[down,right,up,left]
    i=0,j=0
    while count_number<reach_number:
        if list_2d[i][j]==0 and 
    

    return answer

solution(3)