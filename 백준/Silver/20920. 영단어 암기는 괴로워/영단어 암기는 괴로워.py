N, M = map(int, input().split(" "))
l = {}
for i in range(N):
    str1 = input()
    if len(str1) < M:
        continue
    l.setdefault(str1, 0)
    l[str1] += 1

new_l = []
for k, v in l.items():
    new_l.append((v, k))

new_l.sort(key=lambda x: (-x[0], -len(x[1]), x[1]))

for i in range(len(new_l)):
    print(new_l[i][1])