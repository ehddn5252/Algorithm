# 작성일자 : 20210215
# 문제명 : DFS와 BFS
# 문제 요약 :
# 1.  정점의 수, 간선의 수 시작 점 이 주어진다.
# 2. 그 후 연결된 정점이 주어진다. 
# 3. DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하라.

from sys import stdin
from collections import deque

vertex,edge,startPoint=map(int,stdin.readline().split())
vertexMatrix=[[]for _ in range(vertex+1)]
visited1=[0 for _ in range(vertex+1)]
visited2=visited1[:]
for i in range(edge):
    v1,v2 = map(int,stdin.readline().split())
    vertexMatrix[v1].append(v2)
    vertexMatrix[v2].append(v1)
for i in vertexMatrix:
    i.sort()

def DFS(start):
    for i in vertexMatrix[start]:
        if visited1[i]!=1:
            DFSAnswerList.append(i)
            visited1[i]=1
            DFS(i)

def BFS(startPoint):
    queue=deque([startPoint])
    while queue:
        start=queue.popleft()
        BFSAnswerList.append(start)
        for i in vertexMatrix[start]:
            if visited2[i]!=1:
                visited2[i]=1
                queue.append(i)

DFSAnswerList=[startPoint]
BFSAnswerList=[]
visited1[startPoint]=1
visited2[startPoint]=1
DFS(startPoint)

DFSAnswer=""
for i in DFSAnswerList:
    DFSAnswer+=str(i)+" "
print(DFSAnswer)
BFS(startPoint)
BFSAnswer=""
for i in BFSAnswerList:
    BFSAnswer+=str(i)+" "
print(BFSAnswer)

