import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split(" "))
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
duck_positions = []
map1 = []
visit = [[False for _ in range(C)] for _ in range(R)]
q = deque([])
duck_count = 0
ice_q = deque([])
"""
1. 입력시에 오리 위치와 점 위치를 저장해둔다.
1. 오리가 다른 오리를 찾으러 한번 돌아다닌다. 도중에 빙하를 만나면 그 빙하의 위치를 빙하가 녹을 때 사용하는 queue에 넣는다.
2. 오리가 다른 오리를 못 찾았으면 1초가 지난다. 그러고 빙하가 녹는다. 기존의 빙하 q에 있는 것들로만 빙하를 녹이고 빙하가 녹을 때
 그 다음 빙하들을 다른 queue에 저장해두고 다음 오리가 돌아간 후에 녹게 queue를 저장한다.
3. 위를 반복하다가 오리를 찾으면 끝
"""
# 입력부
for r_i in range(R):
    l = list(map(str, input()))
    for c_i in range(len(l)):
        if l[c_i] == 'L':
            duck_positions.append((r_i, c_i))  # row,col
            l[c_i] = '.'
            ice_q.append((r_i, c_i))
        elif l[c_i] == '.':
            ice_q.append((r_i, c_i))
    map1.append(l)

# 오리 시작점
visit[duck_positions[0][0]][duck_positions[0][1]] = True


# 구현부
def BFS():
    ans = 0
    duck_q = deque([duck_positions[0]])
    while True:
        next = deque([])
        # 다른 오리를 찾으러 떠나는 오리
        while duck_q:
            now_r, now_c = duck_q.popleft()
            for i in range(4):
                next_r = now_r + dy[i]
                next_c = now_c + dx[i]

                if next_r >= 0 and next_r < R and next_c >= 0 and next_c < C and not visit[next_r][next_c]:
                    if next_r == duck_positions[1][0] and next_c == duck_positions[1][1]:
                        print(ans)
                        exit(0)
                    if map1[next_r][next_c] == 'X':
                        next.append((next_r, next_c))
                    else:
                        duck_q.append((next_r, next_c))
                    visit[next_r][next_c] = True
        # 다음 오리가 찾을 여정
        duck_q = next
        # 빙하의 수만큼만 q를 pop하기 위해 ice_q를 n에 저장.
        n = len(ice_q)
        ans += 1
        # 빙하가 녹는다.
        while (n != 0):
            n -= 1
            now_r, now_c = ice_q.popleft()
            for i in range(4):
                next_r = now_r + dy[i]
                next_c = now_c + dx[i]
                if next_r >= 0 and next_r < R and next_c >= 0 and next_c < C and not visit[next_r][next_c]:
                    if map1[next_r][next_c] == 'X':
                        map1[next_r][next_c] = '.'
                        ice_q.append((next_r, next_c))


BFS()