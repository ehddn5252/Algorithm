
# 작성일 : 20210105
# 작성자 : 김동우
# 문제명 : 타겟 넘버
# 문제 요약 : 0이아닌 N개의 정수가 있다. 이 수를 적절히 더하거나 빼서 
# 타겟 넘버를 만들어라.

# 문제 풀이 : 
# 1. 완전탐색 사용한다. 모든 경우의 수 다 확인해도 시간초과 안걸리면 성공이다.
# 2. 모든 경우의 수를 확인한다.


def solution(numbers,target):
    
    answer=0
    maxValue = 2**len(numbers)
    for i in range(1,maxValue+1):
        sumValue=0
        confirm=i
        for number in numbers:
            if confirm%2== 0:
                sumValue+=number
            else:
                sumValue-=number
            confirm//=2
        if(sumValue==target):
            answer+=1
    return answer


if __name__ == "__main__":
    answer=solution([1,1,1,1,1],3)
    print(answer)



''' 타인 정답 코드 1
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''

''' 타인 정답 코드 2
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer
'''

'''

def solution(n, t):
    answer = 0
    for i in range(2**len(n)):
        tmp = []
        for j in range(len(n)):
            if i & (2**j) == 0:
                tmp.append(n[j])
            else:
                tmp.append(-1*n[j])
        if sum(tmp) == t:
            answer += 1        
    return answer
'''