n = int(input())
ans = 0
for i in range(n):
    a, b, c = map(int, input().split(" "))
    if a == b and b == c:
        ans = max(10000 + a * 1000, ans)
    elif a == b and b != c:
        ans = max(1000 + b * 100,ans)
    elif a == c and b != c:
        ans = max(1000 + c * 100,ans)
    elif b == c and a != c:
        ans = max(1000 + b * 100,ans)
    else:
        ans = max(ans, 100 * max(a, b, c))

print(ans)