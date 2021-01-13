# 날짜 : 201510704
# 작성자 : 김동우
# 문제명 : 여행 경로
# 문제 해설
# 1. 항상 ICN 공항에서 출발한다.
# 2. tickets읭 각 행[a,b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미이다.
# 3. 주어진 항공권은 모두 사용해야 한다.
# 4. 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return한다.

# 문제풀이 : 백트레킹의 기초문제. 
# 1. 백트레킹으로 처음부터 모든 경우의 수를 다 해본다.
#.2. 
ansList=[]
def recur(destination,answer,tickets):
    answer.append(destination)
    if len(answer)>endCondition:
        return
    if len(answer)==endCondition:
        ansList.append(answer)
        return
    
    '''
    #가지치기
    canFinish=False
    dic={}
    for i in tickets:
        if i[0] not in dic:
            dic[i[0]]=1
        else:
            dic[i[0]]+=1
        if i[1] not in dic:
            dic[i[1]]=1
        else:
            dic[i[1]]+=1
    for i in dic.values():
        if i%2==1:
            canFinish=True
    if canFinish==False:
        return
    '''
    
    for value in tickets:
        if answer[-1]==value[0]:
            inputValue=value[:]
            reducedtickets=tickets[:]
            reducedtickets.remove(value)
            recur(inputValue[1],answer[:],reducedtickets)


def solution(tickets):
    tickets.sort()
    global endCondition
    endCondition=len(tickets)+1
    answer = ["ICN"]
    # 맨 처음이 ICN으로 시작하는 지 확인해서 그렇게 시작하면 알고리즘 들어감 (가지치기의 일종)
    for i in tickets:
        if i[0]!="ICN":
            continue
        sol_reducedtickets=tickets[:]
        sol_reducedtickets.remove(i)
        recur(i[1],answer[:],sol_reducedtickets)
    return ansList[0]
