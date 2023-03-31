num = int(input())

for _ in range(num):
    a,b = map(str,input().split(" "))
    a = int(a)
    print(b[:a-1],end="")
    print(b[a:])