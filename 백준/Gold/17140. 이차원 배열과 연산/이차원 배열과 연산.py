r, c, k = map(int, input().split(" "))
r = r - 1
c = c - 1
l = []
for _ in range(3):
    l.append(list(map(int, input().split(" "))))

time = 0
ans = -1


def is_r_calc():
    global l
    # 열의 수가 더 많거나 같은 경우
    if len(l) >= len(l[0]):
        return True
    else:
        return False


def c_calc():
    global l
    l = list(map(list, zip(*l)))
    r_calc()
    l = list(map(list, zip(*l)))


def r_calc():
    global l, ans
    new_l = []
    max_count = 0
    for i in range(len(l)):
        count_map = {}
        for j in range(len(l[i])):
            if l[i][j] != 0:
                count_map.setdefault(l[i][j], 0)
                count_map[l[i][j]] += 1
        tmp_row = []
        max_count = max(max_count, len(count_map.keys()) * 2)
        if max_count >= 100:
            max_count = 100
        sorted_count_map = sorted(count_map.keys(), key=lambda x: (count_map[x], x))
        for index, key in enumerate(sorted_count_map):
            tmp_row.append(key)
            tmp_row.append(count_map[key])
        new_l.append(tmp_row)

    for i in range(len(new_l)):
        if len(new_l[i]) < max_count:
            for _ in range(max_count - len(new_l[i])):
                new_l[i].append(0)

    l = new_l[:][:]


time = 0
while time <= 100:
    if len(l) > r and len(l[0]) > c and l[r][c] == k:
        ans = time
        break
    if is_r_calc():
        r_calc()
    else:
        c_calc()
    time += 1
print(ans)
