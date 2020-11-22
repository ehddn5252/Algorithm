# 작성일 : 20201122
# 작성자 : 김동우
# 문제명 : 듣보잡
# 문제 요약 : 듣지 못한 사람, 보지 못한 사람의 명단이 각각 주어질때
#            겹치는 인원의 수와 이름을 사전수로 출력하라 
# 문제 해설 :
# 1. 해시를 사용해서 푼다.
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