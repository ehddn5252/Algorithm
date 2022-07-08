t = int(input())
for i in range(t):
    a, b = map(int, input().split(" "))
    start = a
    for i in range(a+1, b+1):
        start = start^i
    print(start)
