# 작성일자 : 20201228
# 작성자 : 김동우
# 문제 : 평균은 넘겠지 (백준 4344)
# 문제 요약 : 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

import sys

def solution():
    outerLoop = int(sys.stdin.readline())
    sumValue=0
    ansList=[]
    for _ in range(outerLoop):
        innerLoop=list(map(int,sys.stdin.readline().split()))
        mean=(sum(innerLoop)-innerLoop[0])/innerLoop[0]
        for index,innerValue in enumerate(innerLoop):
            if index==0:
                pass
            elif innerValue>mean:
                sumValue+=1
        dividedValue=(sumValue/innerLoop[0])*100
        ansList.append(str('%0.3f'%dividedValue)+'%')
        sumValue=0
    for i in ansList:
        print(i)


if __name__ == "__main__":
    solution()