A,B = map(int,input().split(" "))

l = []
s = 0

for i in range(1,100):
    for _ in range(i):
        l.append(i)

for i in range(A-1,B):
    s+=l[i]
print(l)