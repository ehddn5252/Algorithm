"""
색종이 만들기
1. 색종이의 각 부분을 합한다.
2. 합한게 0 또는 n제곱이면 색종이 개수를 추가한다.
3. 아니면 4갈래로 쪼개서 다시 1번 2번 과정을 진행한다.
"""
from collections import deque

num = int(input())
l = [list(map(int, input().split(" "))) for _ in range(num)]

blue_num, white_num = 0, 0

q = deque([[0, 0, num]])
while q:
    x, y, n = q.popleft()
    sum_v = 0
    for x_index in range(x, x + n):
        for y_index in range(y, y + n):
            sum_v += l[x_index][y_index]
    if sum_v == 0:
        white_num += 1
    elif sum_v == n ** 2:
        blue_num += 1
    else:
        q.append([x, y, n // 2])
        q.append([x + n // 2, y, n // 2])
        q.append([x, y + n // 2, n // 2])
        q.append([x + n // 2, y + n // 2, n // 2])
        
print(white_num)
print(blue_num)
