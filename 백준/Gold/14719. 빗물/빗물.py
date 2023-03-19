H, W = map(int, input().split(" "))
l = list(map(int, input().split(" ")))
ans = 0
tmp_ans = 0
start_position = 0
height = 0
start = 0
next_start = 0
find_wall = True
while start < len(l) - 1:
    # 만약에 자신보다
    if find_wall:
        find_wall = False
        height = l[start]
    for j in range(start + 1, len(l)):
        if height <= l[j]:
            next_start = j
            find_wall = True
            break
    if find_wall:
        for j in range(start + 1, next_start):
            ans += max(height - l[j],0)
        start = next_start
    else:
        height -= 1
print(ans)
