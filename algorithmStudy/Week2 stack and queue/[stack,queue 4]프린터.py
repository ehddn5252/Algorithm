# 작성일 : 20201109
# 작성자 : 김동우
# 문제 유형 : stack queue
# 문제 요약 : 프린터는 우선순위에 맞게 인쇄 작업을 수행한다.
# 나머지 인쇄 대기목록에서 j보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣는다. 
# 내가 요청한 문서가 몇 번째로 인쇄되는지 return하라
# 문제 풀이 :
# 1. queue를 만든다.
# 2. 

priorities = [1,1,9,1,1,1]
location=0

def solution(priorities, location):
    # times는 몇번째로 꺼낸 것인지 찾는 변수
    times=0
    queue=[]
    # queue에 [[priority,위치 인덱스],[priority,위치 인덱스],..] 형태로 넣어준다.
    for num,i in enumerate(priorities):
        queue.append((i,num))

    # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
    # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
    # 3. 그렇지 않으면 J를 인쇄합니다.
    # 를 그대로 구현
    while True:
        check=0
        for i in range(len(queue)):
            if queue[0][0]<queue[i][0]:
                queue.append(queue.pop(0))
                check=1
        # 뒤에 중요도가 높은 문서가 하나라도 있는 지 확인한다.
        if check==1:
            continue 
        times+=1
        #
        if queue[0][1]==location:
            return times
        queue.pop(0)