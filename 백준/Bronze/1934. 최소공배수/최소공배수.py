t = int(input())

for _ in range(t):
    ans = 1
    break_flag=False
    A, B = map(int, input().split(" "))
    while True:
        if A==1:
            break_flag=True
        for i in range(2, A + 1):
            if A % i == 0 and B % i == 0:
                A //= i
                B //= i
                ans *= i
                break
            if i==A:
                break_flag=True
        if break_flag:
            ans*=A
            ans*=B
            print(ans)
            break
