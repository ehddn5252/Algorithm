# setting

N, M = map(int,input().split(" "))
l = [[] for _ in range(N)]

answer = 0
ret_flag=False
for _ in range(M):
    a,b = map(int,input().split(" "))
    l[a].append(b)
    l[b].append(a)

def DFS(a,count):
    global l, visit, answer,ret_flag
    if ret_flag:
        return
    if count>=4:
        answer=1
        ret_flag=True
        return

    for i in l[a]:
        if visit[i] == False:
            visit[i] = True
            DFS(i, count+1)
            visit[i] = False

visit = [False for _ in range(N)]
for i in range(N):
    visit[i] = True
    DFS(i,0)
    visit[i] = False

print(answer)
