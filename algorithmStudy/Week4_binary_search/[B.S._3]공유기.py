# 작성일 : 20201125
# 작성자 : 김동우
# 문제명 : 공유기
# 문제 요약 :
# 1. 도현이 집 N개가 수직선 위에 있다.
# 2. 와이파이를 즐기기 위해 공유기 C개를 설치하려고 한다. 
# 3. 와이파이를 즐기기 위한 와이파이의 최대 범위는?
# 문제 본문은 contents.md 참고 

# 문제 풀이 : 
# 1. input 받은 값을 오름차순으로 정렬한다. 
# 2. 가장 왼쪽에 있는 집과 가장 오른쪽에 있는 집 사이의 거리를 구한다.
# 3. 그 거리의 반을 최소 거리로 생각하고 공유기를 설치한다.
# 4. 다 설치 가능하다면 최소 거리를 늘린다.
# 5. 만약 공유기를 다 설치하지 못했다면 최소거리를 줄인다.
# 6. start가 end를 넘기 전까지 계속한다.

# 시간 복잡도 : O(Nlog_2(N))

# 문제 후기 :
# 시간이 더 걸리더라도 풀 수 있는 다른 방법을 찾아보고,
# 그 방법의 시간을 줄이는 데, 이진 탐색을 사용해야 한다.
# 여기서는 최소 길이를 1부터 home의 수만큼 차례로 대입하고 비교하면 풀 수 있으나 
# 시간이 많이 걸린다. 이 최소 길이를 찾는 데, 이진 탐색을 사용해야 한다.
# 아이디어 떠올리기가 어렵다.
import math

# mid(최소거리)를 기준으로 집마다 router를 설치하고 설치된 router의 수를 return한다.
def installRouter(homeList,mid):
    routerConut=1
    beforeInstalled=homeList[0]
    for homeIndex in range(1,len(homeList)):
        if homeList[homeIndex]-beforeInstalled>=mid:
            beforeInstalled=homeList[homeIndex]
            routerConut+=1

    return routerConut

def solution():
    n,theNumberOfRouter=map(int,input().split())
    homeList=[]
    for _ in range(n):
        inputedValue=int(input())
        homeList.append(inputedValue)
    # 1. input 받은 값을 오름차순으로 정렬한다. 
    homeList.sort()

    start = 1
    # 2. 가장 왼쪽에 있는 집과 가장 오른쪽에 있는 집 사이의 거리를 구한다.
    end=homeList[-1]-homeList[0]
    ans = 0

    while(start<=end):
        # 3. 그 거리의 반을 최소 거리로 생각하고 공유기를 설치한다.
        mid=(end+start)//2
        checkRouterNum=installRouter(homeList,mid)
        # 4. 다 설치 가능하다면 최소 거리를 늘린다.
        if(checkRouterNum>=theNumberOfRouter):
            ans=mid 
            start=mid+1
        # 5. 만약 공유기를 다 설치하지 못했다면 최소거리를 줄인다.
        elif(checkRouterNum<theNumberOfRouter):
            end=mid-1
        # 6. start가 end를 넘기 전까지 계속한다.
    print(ans)


if __name__ == "__main__":
    solution()