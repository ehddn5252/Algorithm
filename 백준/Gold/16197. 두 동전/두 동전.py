import heapq
from collections import deque
l = []
coins = []
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
R, C = map(int, input().split(" "))
ans = 11
# 입력
for i in range(R):
    str1 = input()
    for j, v in enumerate(str1):
        if v == 'o':
            coins.append([i, j])
    l.append(str1)

q1 = deque([(0, coins[0][0], coins[0][1], coins[1][0], coins[1][1])])

def is_in(r, c):
    if r >= 0 and r < R and c >= 0 and c < C:
        return True
    else:
        return False


while q1:
    popped = q1.popleft()
    if popped[0] > 10 or popped[0]>=ans:
        continue
    for i in range(4):
        times = popped[0]
        dr1 = popped[1] + dy[i]
        dc1 = popped[2] + dx[i]
        dr2 = popped[3] + dy[i]
        dc2 = popped[4] + dx[i]

        # 정답일 경우
        if (is_in(dr1, dc1) and not is_in(dr2, dc2)) or (not is_in(dr1, dc1) and is_in(dr2, dc2)):
            ans = min(times + 1, ans)
        if times == 10:
            continue
        # 이동하는 경우
        elif is_in(dr1, dc1) and is_in(dr2, dc2):
            if l[dr1][dc1] == "#" and l[dr2][dc2] != "#":
                q1.append((times + 1, popped[1], popped[2], dr2, dc2))
            elif l[dr1][dc1] != "#" and l[dr2][dc2] == "#":
                q1.append((times + 1, dr1, dc1, popped[3], popped[4]))
            elif l[dr1][dc1] != "#" and l[dr2][dc2] != "#":
                q1.append((times + 1, dr1, dc1, dr2, dc2))
        # 정답 확인

if ans == 11:
    print(-1)
else:
    print(ans)
