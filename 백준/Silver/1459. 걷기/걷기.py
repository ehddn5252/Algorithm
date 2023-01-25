x, y, w, s = map(int, input().split(" "))
ans = 0

if w <= s < 2 * w:
    ans = min(x, y) * s + abs(x - y) * w
elif s <= w:
    ans = min(x, y) * s + abs(x - y) // 2 * s * 2 + abs(x - y) % 2 * w
elif 2 * w <= s:
    ans = (x + y) * w
print(ans)
