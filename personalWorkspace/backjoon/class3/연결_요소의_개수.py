# 작성일자 : 20210215
# 문제명 : 연결 요소의 개수
# 문제 풀이 : 전형적인 DFS 문제이다.

from sys import stdin
import sys
limit_number = 150000
sys.setrecursionlimit(limit_number)

def DFS(vertex):
    for vertexValue in vertexDic[vertex]:
        if visited[vertexValue]!=1:
            visited[vertexValue]=1
            DFS(vertexValue)


vertex,edge=map(int,stdin.readline().split())
vertexDic=[[] for _ in range(vertex+1)]
visited=[0 for _ in range(vertex+1)]
answer=0
for i in range(edge):
    v1,v2=map(int,stdin.readline().split())
    vertexDic[v1].append(v2)
    vertexDic[v2].append(v1)
for i in range(1,vertex+1):
    if visited[i]==0:
        answer+=1
    DFS(i)
print(answer)
