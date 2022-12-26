num = int(input())  # 사람수
a, b = map(int, input().split(" "))  # 촌수를 계산해야 하는 두 사람 번호
m = int(input())  # 자식간의 관계 수 m

l = [[] for _ in range(num + 1)]
for i in range(m):
    input1, input2 = map(int, input().split(" "))
    l[input1].append(input2)
    l[input2].append(input1)

visit = [False for i in range(num + 1)]

def dfs(v, cnt):
    cnt += 1
    visit[v] = True

    for i in l[v]:
        if i == b:
            print(cnt - 1)
            exit()
        if not visit[i]:
            dfs(i, cnt)

dfs(a, 1)
print(-1)
