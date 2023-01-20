testcase = int(input())

for _ in range(testcase):
    M, N, x, y = map(int, input().split(" "))
    ans = -1
    gcd = 1
    for i in range(1, M + 1):
        if M % i == 0 and N % i == 0:
            gcd = i
    lcm = M * N // gcd

    while True:
        if x % N == y % N:
            ans = x
            break
        if x > lcm:
            ans = -1
            break

        x += M
    print(ans)
