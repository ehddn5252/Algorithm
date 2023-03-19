n = int(input())
start = list(input())
ans = 0
for _ in range(n - 1):
    compare = start[:]
    new_word = input()
    cnt = 0

    for w in new_word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    if cnt < 2 and len(compare) < 2:
        ans += 1

print(ans)
