A, B, C = map(int, input().split(" "))
map1 = {}

def shuffle(a, b):
    x = min(a, b)
    y = max(a, b)
    return 2 * x, y - x

ans = 0
while True:
    if A == B and B == C:
        ans = 1
        break
    if A != B:
        A, B = shuffle(A, B)
    if B != C:
        B, C = shuffle(B, C)
    if A != C:
        C, A = shuffle(C, A)

    key = str(A) + " " + str(B) + " " + str(C)
    if map1.get(key) is None:
        map1[key] = True
    else:
        break
print(ans)
