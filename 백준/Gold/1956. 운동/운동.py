INF = 9999999
V, E = map(int, input().split(" "))

l = [[INF for i in range(V)] for _ in range(V)]
# 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오.
for i in range(E):
    a, b, c = map(int, input().split(" "))
    l[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if l[i][k] + l[k][j] < l[i][j]:
                l[i][j] = l[i][k] + l[k][j]

ans = INF
for i in range(V):
    if l[i][i] < ans:
        ans = l[i][i]
if ans==INF:
    print(-1)
else:
    print(ans)