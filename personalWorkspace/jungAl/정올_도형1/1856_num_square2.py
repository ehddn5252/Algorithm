n, m = map(int, input().split(" "))

num=1
for i in range(n):
    if (i%2 == 0):
        for _ in range(m):
            print(str(num)+" ", end="")
            num += 1
    else:
        tmp_num = num-1
        for j in range(tmp_num+m, tmp_num, -1):
            print(str(j) + " ", end="")
            num += 1

    print()
