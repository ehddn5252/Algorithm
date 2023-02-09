N, X = map(int, input().split(" "))
l = list(map(int, input().split(" ")))

tmp = sum(l[:X])
max_value = 0
ans2 = 0
for i in range(len(l) - X+1):
    if i!=0:
        tmp = tmp - l[i - 1] + l[i + X - 1]
    if max_value <= tmp:
        max_value = tmp
tmp = sum(l[:X])
for i in range(len(l) - X+1):
    if i!=0:
        tmp = tmp - l[i - 1] + l[i + X - 1]
    if max_value <= tmp:
        ans2 += 1
        max_value = tmp

if max_value != 0:

    print(max_value)
    print(ans2)
else:
    print("SAD")
