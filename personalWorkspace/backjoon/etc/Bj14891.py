def rotate(com):
    global gears

    visit = [False, False, False, False]
    q = []
    q.append(com)
    while q:
        command = q.pop()
        gear_num, direction = command[0], command[1]
        visit[gear_num] = True
        # 반시계방향
        if direction == -1:

            if gear_num + 1 < 4 and not visit[gear_num + 1] and gears[gear_num][2] != gears[gear_num + 1][6]:
                q.append([gear_num + 1, 1])
            if gear_num - 1 >= 0 and not visit[gear_num - 1] and gears[gear_num][6] != gears[gear_num - 1][2]:
                q.append([gear_num - 1, 1])
            tmp = gears[gear_num][0]
            for i in range(len(gears[gear_num]) - 1):
                gears[gear_num][i] = gears[gear_num][i + 1]
            gears[gear_num][-1] = tmp
        # 시계 방향
        else:
            if gear_num + 1 < 4 and not visit[gear_num + 1] and gears[gear_num][2] != gears[gear_num + 1][6]:
                q.append([gear_num + 1, -1])
            if gear_num - 1 >= 0 and not visit[gear_num - 1] and gears[gear_num][6] != gears[gear_num - 1][2]:
                q.append([gear_num - 1, -1])
            tmp = gears[gear_num][-1]
            for i in range(len(gears[gear_num]) - 1, 0, -1):
                gears[gear_num][i] = gears[gear_num][i - 1]
            gears[gear_num][0] = tmp

gears = [[],[],[],[]]
for i in range(4):
    t = input()
    for j in range(len(t)):
        gears[i].append(t[j])

n = int(input())
commands = []
for i in range(n):
    g, d = map(int, input().split(" "))
    commands.append([g - 1, d])

for command in commands:
    rotate(command)

start = 1
ans = 0
for i in range(4):
    if gears[i][0] == '1':
        ans += start
    start *= 2

print(ans)