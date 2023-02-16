n = int(input())
map1 = []
for i in range(n):
    map1.append(input())

find_head = False
heart = []
for i in range(len(map1)):
    for j in range(len(map1[i])):
        if not find_head and map1[i][j] == '*':
            find_head = True
            heart = [i + 1, j]

left = 0
while True:
    if 0 <= heart[1] + left < n and map1[heart[0]][heart[1] + left] == '*':
        left -= 1
    else:
        left += 1
        break

right = 0
while True:
    if heart[1] + right < n and map1[heart[0]][heart[1] + right] == '*':
        right += 1
    else:
        right -= 1
        break

down = 0

while True:
    if 0 <= heart[0] + down < n and map1[heart[0] + down][heart[1]] == '*':
        down += 1
    else:
        down -= 1
        break

left_lag = 0

right_lag = 0
while True:
    if 0 <= heart[0] + down + left_lag + 1 < n and map1[heart[0] + down + left_lag + 1][heart[1] - 1] == '*':
        left_lag += 1
    else:
        break

while True:
    if 0 <= heart[0] + down + right_lag + 1 < n and map1[heart[0] + down + right_lag + 1][heart[1] + 1] == '*':
        right_lag += 1
    else:
        break

print(heart[0]+1, heart[1]+1)
print(abs(left), abs(right), abs(down), abs(left_lag), abs(right_lag))
