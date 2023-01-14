from collections import deque


def dfs(popped, cnt, ans_list):
    if cnt == n:
        print(" ".join( str(i) for i in list(ans_list)))
        exit(0)
    for i in range(n):
        if l[i] == popped * 2 and not visit[i]:
            visit[i] = True
            ans_list.append(popped * 2)
            dfs(popped * 2, cnt + 1, ans_list)
            ans_list.pop()
            visit[i] = False
        if popped % 3 == 0 and l[i] == popped // 3 and not visit[i]:
            visit[i] = True
            ans_list.append(popped // 3)
            dfs(popped // 3, cnt + 1, ans_list)
            ans_list.pop()
            visit[i] = False


n = int(input())
l = list(map(int, input().split(" ")))
visit = [False for _ in range(n)]

for i in range(n):
    visit[i] = True
    dfs(l[i], 1, deque([l[i]]))
    visit[i] = False
