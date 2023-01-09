from collections import deque

l = list(map(int, input().split(" ")))
l = deque([l])

map1= {}
ans = 0
while l:
    A, B, C = map(int, sorted(l.popleft()))
    if A == B == C:
        ans = 1
        break
    key = str(A)+" "+ str(B)+" "+str(C)
    if map1.get(key) is None:
        map1[key] = True
    else:
        continue
    if A != B:
        l.append([A + A, B - A, C])
    if B != C:
        l.append([A, B + B, C - B])
    if A != C:
        l.append([A + A, B, C - A])

print(ans)