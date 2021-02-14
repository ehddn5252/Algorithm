# 작성일자 : 20210214
# 문제명 : 입국심사
# 문제 요약 :
# 1. n 명이 입국심사를 위해 기다리고 있다.
# 2. 처음에 모든 심사대는 비어있다.
# 3. 한 심사대에서는 동시에 한 명만 심사를 할 수 있다.
# 4. 가장 앞에 서 있는 사람은 비어 있는 심사대로 간다.
# 5. 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사받는다.
# 6. 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하자
# 입력 : 입국 기다리는 사람 수 n, 각 심사관이 한명을 걸리는 시간이 담긴 배열 times
    
# 문제 풀이 : 
# 1. 일단 최대 시간이 입국 심사대에서 가장 짧은 줄로 모든 사람을 돌렸을 때이다. maxTime = times*n 으로 잡는다.
# 2. start = 1, end = maxTime, mid = (start+end)//2 로 설정한다.
# 3. start보다 end가 작거나 같으면 계속 도는 while문 만들고
# 4. mid(시간의 중간값) // 심사대에서 걸리는 시간 하면 그 심사대에서 몇 명을 처리했는 지 알 수 있다.
# 5. 만약 심사대에서 처리한 수가 n보다 크거나 같다면 정답에 저장하고 start=mid+1로 설정 (bisearch)
# 6. 만약 심사대에서 처리한 수가 n보다 작다면 end=mid-1로 두고 다시 while문을 돈다.
# 7. 이렇게 해서 돌다보면 start가 end보다 커지는 순간에 값을 출력한다.
#    answer값은 처리한 사람의 수가 대기 인원보다 더 많거나 같을 때의 걸린 시간으로 저장되는 데,
#    이때를 정답으로 한 것이 처리한 사람이 더 적을때 걸린 시간은 처리를 못했으니 아예 정답이 안되고
#    처리한 인원이 더 많을 때는 시간을 줄여야 하는데, 계속 줄이다 보면 정답에 수렴한다.
#  
def solution(n, times):
    answer = 0
    # 1. 일단 최대 시간이 입국 심사대에서 가장 짧은 줄로 모든 사람을 돌렸을 때이다. maxTime = times*n 으로 잡는다.
    maxTime=min(times)*n
    # 2. start = 1, end = maxTime, mid = (start+end)//2 로 설정한다.
    start = 1
    end = maxTime
    # 3. start보다 end가 작거나 같으면 계속 도는 while문 만들고
    while start<=end:
        mid = (start+end)//2
        comparePeople=0
        for i in times:
            # 4. mid(시간의 중간값) // 심사대에서 걸리는 시간 하면 그 심사대에서 몇 명을 처리했는 지 알 수 있다.
            comparePeople+=mid//i
            # 5. 만약 심사대에서 처리한 수가 n보다 크거나 같다면 정답에 저장하고 start=mid+1로 설정 (bisearch)
            if comparePeople>=n:
                answer=mid
                end=mid-1   
                break
        # 6. 만약 심사대에서 처리한 수가 n보다 작다면 end=mid-1로 두고 다시 while문을 돈다.
        if comparePeople<n:
            start=mid+1
    return answer

if __name__=="__main__":
    answerList=[28,15,15,15,1000000000]
    nums=[6,20,10,11,1]
    times=[[7,10],[1,4,5],[3,4,5],[3,4,5],[1000000000]]
    i=1
    for num,time,answer in zip(nums,times,answerList):
        print(i)
        i+=1
        print(f'answer : {answer}, mysolve:{solution(num, time)}')
    