n = int(input())

l = list(map(int, input().split(" ")))
map1 = {}
for i in l:
    map1.setdefault(i, 0)
    map1[i] += 1

ans = 0
check_nums = set([])
for i in range(n):
    for j in range(i + 1, n):
        if map1.get(l[i] + l[j]) is not None:
            if (l[j] == 0 and l[i] == 0 and map1[0] == 2) or (l[i]==0 and map1[l[j]]==1) or (l[j]==0 and map1[l[i]]==1):
                continue
            check_nums.add(l[i] + l[j])
while check_nums:
    ans += map1[check_nums.pop()]

print(ans)
