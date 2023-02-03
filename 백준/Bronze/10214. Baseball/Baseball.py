testcase = int(input())

for i in range(testcase):
    sum_a = 0
    sum_b = 0
    for _ in range(9):
        a,b = map(int,input().split(" "))
        sum_a+=a
        sum_b+=b
    if sum_a>sum_b:
        print("Yonsei")
    elif sum_a<sum_b:
        print("Korea")
    else:
        print("Draw")