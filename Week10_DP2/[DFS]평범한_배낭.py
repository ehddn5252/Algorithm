# 작성일자 : 20210124
# 작성자 : 김동우
# 문제 요약 : 첫줄에 물품의 수 (N)와 배낭의 무게(K)가 주어지고 
# 그 다음부턴 물건의 무게와 가치가 주어진다.
# 물건의 무게 합이 배낭의 무게를 넘지 않을 때 배낭에 가장 큰 가치를
# 출력하시오 
# 알고리즘 : DFS -> 시간초과
#  
maxValue=0
K=0
def DFS(currentWeight,currentValue,visited,weightAndValue):
    global maxValue,K

    if currentWeight>K:
        return

    if maxValue<currentValue:
        maxValue=currentValue

    for index,value in enumerate(weightAndValue):
        if visited[index]!=1:
            visited[index]=1
            DFS(currentWeight+value[0],currentValue+value[1],visited,weightAndValue)
            visited[index]=0

def solution():
    global K
    N,K=list(map(int,input().split()))
    weightAndValue=[]

    for _ in range(N):
        weightAndValue.append(list(map(int,input().split()))) 
    
    visited=[0]*N
    for index,value in enumerate(weightAndValue):
        visited[index]=1
        DFS(value[0],value[1],visited,weightAndValue)
        visited[index]=0
    global maxValue
    print(maxValue)


if __name__ =="__main__":
    solution()
