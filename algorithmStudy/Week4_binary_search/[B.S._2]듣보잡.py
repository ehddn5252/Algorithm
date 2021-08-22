# 작성일 : 20201122
# 작성자 : 김동우
# 문제명 : 듣보잡
# 문제 요약 : 듣지 못한 사람, 보지 못한 사람의 명단이 각각 주어질때
#            겹치는 인원의 수와 이름을 사전수로 출력하라 
# 문제 해설 : 해시를 사용해서 푼다.
# 1. 듣지 못한 사람 dictionary를 저장한다. 
# 2. ditionary를 사전순으로 정렬한다.
# 3. 보도 못한 사람을 한번 돌면서 dictionary에 보도 못한 사람이 있으면 1 없으면 0을 ansList에 append한다.
# 4. ansList의 요소를 하나씩 출력한다
# 시간 복잡도 : O(N) 
# clear

def solution():
    N,M=map(int,input().split())
    notHear={}
    inputedString=""

    # 듣도못한
    for _ in range(N):
        inputedString=str(input())
        notHear[inputedString]=1
    ansList=[]

    # 보도 못한
    for _ in range(M):
        inputedString=str(input())
        if  notHear.get(inputedString):
            ansList.append(inputedString)

    ansList.sort()
    print(len(ansList))
    for deudbojab in ansList:
        print(deudbojab)

if __name__ == "__main__":
    solution()

