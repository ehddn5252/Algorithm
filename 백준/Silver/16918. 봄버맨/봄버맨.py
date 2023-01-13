R, C, N = map(int, input().split(" "))
l = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visit = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    s = input()
    l.append([])
    for j in range(C):
        if s[j]=='O':
            visit[i][j]=3
        l[i].append(s[j])
second = 1
while second < N:
    second += 1
    if second%2==0:
        for i in range(R):
            for j in range(C):
                if l[i][j] == '.':
                    l[i][j] = 'O'
                    visit[i][j] = second+3
    else:
        for i in range(R):
            for j in range(C):
                if l[i][j] == 'O' and second==visit[i][j]:
                    l[i][j] = '.'
                    for k in range(4):
                        next_i = i + dx[k]
                        next_j = j + dy[k]
                        if next_i >= 0 and next_i < R and next_j >= 0 and next_j < C:
                            if l[next_i][next_j] == 'O' and second!=visit[next_i][next_j]:
                                l[next_i][next_j] = '.'


for i in range(R):
    for j in range(C):
        print(l[i][j],end="")
    print("")
