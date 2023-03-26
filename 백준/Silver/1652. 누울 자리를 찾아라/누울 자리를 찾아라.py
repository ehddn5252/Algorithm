N = int(input())
l = []
for i in range(N):
    s = input()
    tmp = []
    for j in range(len(s)):
        tmp.append(s[j])
    l.append(tmp)
import copy
new_l = copy.deepcopy(l)
length = 0  # 세로
width = 0  # 가로
for i in range(N):
    for j in range(N):
        if l[i][j] == '.' and j + 1 < N and l[i][j + 1] == '.':
            width += 1
            for k in range(j, N):
                if l[i][k] == '.':
                    l[i][k] = 'X'
                else:
                    break
for j in range(N):
    for i in range(N):
        if new_l[i][j] == '.' and i + 1 < N and new_l[i + 1][j] == '.':
            length += 1
            for k in range(i, N):
                if new_l[k][j] == '.':
                    new_l[k][j] = 'X'
                else:
                    break


print(width, length)
