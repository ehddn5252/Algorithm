n = int(input())
max_value = 0
ans = 0
q = []
map1 = {}
for _ in range(n):
    before_position, high = map(int, input().split(" "))
    if map1.get(high) is None:
        if high != 0:
            ans += 1
        map1[high] = 1
    if max_value < high:
        max_value = high

    else:
        items = list(map1.items())
        for k, v in items:
            if k > high:
                map1.pop(k)
print(ans)