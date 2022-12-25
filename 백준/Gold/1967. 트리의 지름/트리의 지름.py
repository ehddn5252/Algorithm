import sys
sys.setrecursionlimit(30000)
num = int(sys.stdin.readline())

l = [[] for _ in range(num + 1)]
ans = 0
end = 0

def dfs(start, weight):
    global ans, end
    if visit[start]:
        return
    visit[start] = 1
    if weight > ans:
        ans = weight
        end = start
    for i in l[start]:
        if visit[i[0]] == 0:
            dfs(i[0], weight+i[1])


for i in range(num - 1):
    parent, child, weight = map(int, sys.stdin.readline().split(" "))
    l[parent].append((child, weight))
    l[child].append((parent, weight))

visit = [0 for _ in range(num + 1)]
dfs(1,0)
visit = [0 for _ in range(num + 1)]
dfs(end,0)
print(ans)