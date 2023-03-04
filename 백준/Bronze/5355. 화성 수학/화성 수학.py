testcase = int(input())

for _ in range(testcase):
    l = list(map(str, input().split(" ")))
    ans = 1
    for i in range(len(l)):
        if l[i] == '@':
            ans *= 3
        elif l[i] == '%':
            ans += 5
        elif l[i] == '#':
            ans -= 7
        else:
            ans *= float(l[i])
    print("{:.2f}".format(ans))