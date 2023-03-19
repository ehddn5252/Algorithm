n, m = map(str, input().split(" "))

map1 = {}
for i in range(int(n)):
    map1.setdefault(input(), 0)

total_num = len(map1.keys())
ans = 0
if m == "Y":
    ans = total_num

elif m == "F":
    ans = total_num // 2
else:
    ans = total_num // 3

print(ans)
