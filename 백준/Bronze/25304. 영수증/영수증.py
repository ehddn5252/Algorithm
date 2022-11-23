receipt = int(input())
n = int(input())

for i in range(n):
    price, num = map(int, input().split(" "))

    receipt -= price * num

if receipt == 0:
    print("Yes")
else:
    print("No")
