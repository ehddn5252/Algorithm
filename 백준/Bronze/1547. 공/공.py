n = int(input())
position = 1
for i in range(n):
    a, b = map(int, input().split(" "))
    if a == position:
        position = b
    elif b == position:
        position = a

print(position)
