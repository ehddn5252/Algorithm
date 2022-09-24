import math
num = int(input())
l = list(map(int, input().split(" ")))

multi = 1
for i in l:
    multi *= i

l.sort()
if num%2==0:
    print(l[-1]*l[0])
    #print(math.ceil(multi**(1/(num/2))))
elif num==1:
    print(l[0]**2)
else:
    print(l[(num // 2)]**2)
