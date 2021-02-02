# 작성일 : 20201109
# 작성자 : 김동우
# 문제 유형 : stack queue
# 문제 요약 : 프린터는 우선순위에 맞게 인쇄 작업을 수행한다.
# 나머지 인쇄 대기목록에서 j보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣는다. 
# 내가 요청한 문서가 몇 번째로 인쇄되는지 return하라
# 문제 풀이 :
# 1. queue를 만든다.
# 그냥 설명대로 구현

priorities = [1,1,9,1,1,1]
location=0

def solution(priorities, location):
    times=0
    queue=[]
    for num,i in enumerate(priorities):
        queue.append((i,num))
    print(queue[0][0])
    while True:
        for i in range(len(queue)):
            if queue[0][0]<queue[i][0]:
                tmp=queue.pop(0)
                queue.insert(-1,tmp)
        times+=1
        if queue[0][1]==location:
            return times
        queue.pop(0)

print(solution(priorities, location))