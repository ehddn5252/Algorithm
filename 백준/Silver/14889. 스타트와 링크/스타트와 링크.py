from itertools import combinations, permutations

n = int(input())
l = [list(map(int, input().split(" "))) for _ in range(n)]
l2 = [i for i in range(1, n + 1)]

ans = 999999
for i in combinations(l2, n // 2):
    team1 = 0
    team2 = 0
    visit = [False for _ in range(n)]
    team2_l=[]
    for s in i:
        visit[s-1]=True
    for k,v in enumerate(visit):
        if not v:
            team2_l.append(k)
    for j in combinations(i, 2):
        a, b = j
        team1 += l[a - 1][b - 1]
        team1 += l[b - 1][a - 1]
    for j in combinations(team2_l,2):
        a, b = j
        team2 += l[a][b]
        team2 += l[b][a]

    if abs(team2 - team1) < ans:
        ans = abs(team2 - team1)

print(ans)
