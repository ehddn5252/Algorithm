tmp = []
for i in range(8):
    tmp.append(input())

l = []
while tmp:
    l.append(list(tmp.pop()))

l[0][0] = 'S'

from collections import deque

dx = [0, 0, -1, 1, 0, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, 0, -1, -1, 1, 1]
q = deque([(0, 0, 0)])
first= 0
while q:
    round,x, y = q.popleft()

    if round!=first:
        first=round
        for j in range(7):
            for k in range(8):
                if l[j + 1][k] == '#':
                    l[j][k] = '#'
                elif l[j + 1][k] == '.':
                    if l[j][k] != 'S':
                        l[j][k] = '.'
                elif l[j + 1][k] == 'S':
                    if l[j][k] != 'S':
                        l[j][k] = '.'
        for j in range(8):
            if l[7][j] != 'S':
                l[7][j] = '.'
    if round==8:
        break
    if l[x][y] == 'S':
        for i in range(9):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x >= 0 and next_x < 8 and next_y >= 0 and next_y < 8:
                if l[next_x][next_y] != '#':
                    l[next_x][next_y] = 'S'
                    q.append((round+1,next_x, next_y))

ans = 0
for i in range(8):
    for j in range(8):
        if l[i][j] == 'S':
            ans = 1
print(ans)
