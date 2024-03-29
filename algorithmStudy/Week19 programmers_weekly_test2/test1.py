# 작성 일자 : 20210507
# 작성자 : 김동우
# 문제명 : 모두 0으로 만들기
# 문제 요약 : 각 점에 가중치가 부여된 트리가 주어진다. 다음 연산을 통해 가중치를 0으로 만들고자 한다.
# 임의의 연결된 두 점을 골라서 한 쪽은 1 증가시키고 한 쪽은 1 감소시킨다.
# 모든 트리가 위의 행동을 통해 0으로 만들 수 있는 것이 아니다. 최소 몇 번만에 가능한 지 찾아 return
# 만약 불가능하다면 -1을 리턴하라. 

# 문제 풀이 : 
# 음..모든 노드가 연결되어 있으면 어떻게든 0으로 만들 수 있다.
# 방법1. 연결된 노드에 모든 값을 건네 주기.
# 한 노드에 여러개의 노드가 저장되어 있다면 하나의 노드로 값을 계속 이동시켜야 한다.
# 여기서 중요한 점은 가운데 있는 노드로 이동해야한다. 입출력 예시를 보자

'''
a   	        edges	                    result
[-5,0,2,1,2]	[[0,1],[3,4],[2,3],[0,3]]	9
'''

# 위의 예시를 보면 2번노드에 있는 것과 4번 노드에 있는 것을 3번노드로 옮기면 4번 움직이고 3번노드는 4가 된다. 또 이를 0번 노드와 연산하면 총 9가 된다.
# 이를 알고리즘으로 어떻게 옮길까..?
# 일단 가장 연결된 곳이 많은 노드에 저장한다. 그리고 연결되어 있는 것이 적은 순서대로 이동시킨다.
# 즉 리프노드부터 쭉 이동시키면 된다.
#  


def solution(a, edges):
    # 일단 sum(a)는 0이어야 답이 될 수 있다.
    if sum(a)!=0:
        return -1
    answer=0
    a_index=[0 for i in range(a)]
    for edge in edges:
        a_index[edge[0]]+=1
        a_index[edge[1]]+=1

    for index,value in enumerate(a_index):
        if value==1:
            answer+=a[index]
            a[index]=0

    for index,start_edge in enumerate(a):
        answer-=a[index]
        for i in edges :
            


    return answer