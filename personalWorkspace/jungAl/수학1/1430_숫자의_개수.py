a = int(input())
b = int(input())
c = int(input())

m = a * b * c

map1={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
while m>=1:
    tmp = m%10
    map1[tmp] += 1
    m //= 10

for k, v in map1.items():
    print(v)