from collections import deque

num = int(input())  # 사람수
a, b = map(int, input().split(" "))  # 촌수를 계산해야 하는 두 사람 번호
m = int(input())  # 자식간의 관계 수 m

l = [[0 for _ in range(num + 1)] for _ in range(num + 1)]
for i in range(m):
    input1, input2 =  map(int, input().split(" "))
    l[input1].append(input2)
    l[input2].append(input1)

q = deque([[a, 0]])
visit = [False for i in range(num + 1)]
break_flag = False
while q:
    popped = q.popleft()
    node = popped[0]
    visit[node] = True
    ret = popped[1]
    if node == b:
        print(ret)
        break_flag = True
        break
    for i in l[node]:
        if not visit[i]:
            q.append([i, ret + 1])

if not break_flag:
    print(-1)
