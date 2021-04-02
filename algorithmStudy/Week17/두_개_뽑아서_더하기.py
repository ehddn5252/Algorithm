# 작성일자 : 20210402
# 문제명 : 두 개 뽑아서 더하기
# 문제 요약 : 정수 배열이 주어진다.
# 1. 서로 다른 인덱스에 있는 두개의 수를 뽑아 더해서 만들 수 있는 모든 수를 오름차순으로 담아라. 


def solution(numbers):
    answer = []
    for index1,value1 in enumerate(numbers):
        for index2,value2 in enumerate(numbers):
            if index1!=index2:
                answer.append(value1+value2)
    answer=list(set(answer))
    answer.sort()
    print(answer)
    return answer