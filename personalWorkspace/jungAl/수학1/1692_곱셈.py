n = int(input())
m = int(input())
s = 0
des = 1
while m>1:
    s += (m % 10 * n)*des
    print(m % 10 * n)
    des *= 10
    m//=10
print(s)