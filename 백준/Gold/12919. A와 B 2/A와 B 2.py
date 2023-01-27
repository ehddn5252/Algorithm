str_a = input()
str_b = input()

map_b = {"A": 0, "B": 0}

for i in range(len(str_b)):
    map_b[str_b[i]] += 1

map_a = {"A": 0, "B": 0}
for i in range(len(str_a)):
    map_a[str_a[i]] += 1

ans = 0


def dfs(str_tmp, map_a_inner):
    global ans, map_b, str_b
    if str_tmp == str_b:
        ans = 1
        return
    if len(str_tmp) > len(str_b):
        return
    if map_a_inner['A'] > map_b['A'] or map_a_inner['B'] > map_b['B']:
        return
    in_check = False
    if str_tmp in str_b or str_tmp[::-1] in str_b:
        in_check = True
    if not in_check:
        return
    map_a_inner['A'] += 1
    dfs(str_tmp + "A", map_a_inner)
    map_a_inner['A'] -= 1

    map_a_inner['B'] += 1
    dfs((str_tmp + "B")[::-1], map_a_inner)
    map_a_inner['B'] -= 1


dfs(str_a, map_a)
print(ans)
