a, b = map(int, input().split())
ans = 1
i = 2
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        ans *= i
        a //= i
        b //= i
        i = 1
    i += 1

print(a*b*ans)
