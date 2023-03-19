def find(a, b):
    x = 2
    limit = min(a, b)
    while x <= limit:
        if a % x == 0 and b % x == 0:
            a /= x
            b /= x
            x = 2
        else:
            x += 1
    return int(a), int(b)


n = int(input())

l = list(map(int, input().split(" ")))

for i in range(1, len(l)):
    a, b = find(l[0], l[i])
    print(f"{a}/{b}")
