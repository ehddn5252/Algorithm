n = int(input())
l = []
for _ in range(n):
    l.append(input())


def find_2_friend(input_i):
    global n, visit
    for k in range(n):
        if l[input_i][k] == 'Y':
            visit[k] = True


max_ans = 0
for i in range(n):
    visit = [False for _ in range(n)]
    for j in range(n):
        if l[i][j] == "Y":
            visit[j]=True
            find_2_friend(j)
    visit[i]=False
    max_ans = max(max_ans, sum(visit))

print(max_ans)
