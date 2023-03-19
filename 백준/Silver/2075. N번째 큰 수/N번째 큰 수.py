n = int(input())
l = list(map(int, input().split(" ")))
for _ in range(n - 1):
    for i in list(map(int, input().split(" "))):
        l.sort()
        if i>l[0]:
            del l[0]
            l.append(i)

print(l[0])
