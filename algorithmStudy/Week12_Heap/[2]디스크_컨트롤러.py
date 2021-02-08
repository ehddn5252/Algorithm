# 작성일자 : 20210208
# 문제명 : [프로그래머스 힙] 디스크 컨트롤러 
# 문제 요약 : 
# 하드 디스크는 한 번에 하나의 작업만 수행할 수 있다. 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은
# 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 
# 평균이 얼마가 되는지 구하시오
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리한다.

'''
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

'''

# 문제 풀이 : 
# 1. 시작하는 작업의 시작하는 시간 + 걸리는 시간(jobs[index][0]+jobs[index][1])이 
# 그 다음 시작하는 작업의 시작 시간보다 작으면 그 다음 시작하는 작업의 걸리는 시간을 더한다.
# 2. 시작하는 작업의 시작하는 시간 + 걸리는 시간(jobs[index][0]+jobs[index][1])이
# 그 다음 시작하는 작업의 시작 시간보다 크면 전체 중 걸리는 시간이 가장 작은 것을 찾아서 time에 time - 시작시간(start) + 걸리는시간을 더한다.
#  
import heapq

def solution(jobs):
    
    jobs.sort(key= lambda x:(x[0],x[1]))
    jobsLen=len(jobs)
    index=0
    time=jobs[0][0]+jobs[0][1]
    answer = jobs[0][1]
    jobs.pop(0)
    while jobs:
        #print(time)
        if time<=jobs[0][0]:
            time+=jobs[0][1]
            answer += jobs[0][1]
            #print(jobs[0])
            jobs.pop(0)
        else:
            minValue=9876543210
            minindex=0
            for i in range(len(jobs)):
                if time>jobs[i][0] and minValue>jobs[i][1]:
                    minindex=i
                    minValue=jobs[i][1]
            answer+=time+jobs[minindex][1]-jobs[minindex][0]
            time +=jobs[minindex][1]
            #print(jobs[minindex])
            jobs.pop(minindex)
    #print(time)
    #print(f'{answer//jobsLen}')
    return answer//jobsLen
    #print(time//jobsLen)

if __name__=="__main__":
    test1=[[0, 3], [3, 5], [2, 3], [2, 8]] # 2
    test2=[[0,1],[0,1],[1,0]] # 1
    test3 = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]] # 72
    test4 = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]] # 72
    jobs=[[0, 3], [1, 9], [2, 6]]
    testcaseList=[test1,test2,test3,test4,jobs]
    for testcase in testcaseList:
        solution(testcase)
    
    # return = 9
