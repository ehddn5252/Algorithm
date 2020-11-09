# 작성 날짜 : 20201109
# 작성자 : 김동우
# 문제 이름 : 기능 개발
# 문제 유형 : stack, queue
# 문제 요약 : 기능별 개선 작업 수행 중이다. 기능이 100일때 배포를 할 수 있고,
# 1. 현재 몇 퍼센트 완료 되었는 지, 2. 하루 기능 작업 속도 주어진다
# 뒷 기능은 앞의 기능이 완료되면 같이 배포된다고 하면 각 배포할마다 몇 개의 기능이 배포되는 지 구하기
# 풀이1
# 1. 100에서 현재 진행률을 뺀다.
# 2. 그 값을 speeds[i]로 나눈다
# 3. 그럼 남은 날짜가 나온다. 
# 시간 복잡도 : O(N)
# 삽질1 
# 정수형으로 나누는 //를 사용해서 걸리는 시간이 실수형으로 나올 때를 무시했다. (TESTCASE11)

import math

def solution(progresses, speeds):
    answer = []
    publish=1
    takenTime=progresses
    for i in range(len(progresses)):
        takenTime[i]=math.ceil((100-progresses[i])/(speeds[i]))
    object1=takenTime[0]

    for i in range(1,len(takenTime)):
        if object1>=takenTime[i]:
            publish+=1
        else:
            answer.append(publish)
            object1=takenTime[i]
            publish=1
        if i==len(takenTime)-1:
            answer.append(publish)
    return answer
