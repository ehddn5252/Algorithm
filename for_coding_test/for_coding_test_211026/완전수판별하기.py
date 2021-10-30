# 완전수 판별하기

import math
num = int(input())
answer=0
squared_root: int = int(math.sqrt(num))
for i in range(1,squared_root+1):
    if num%i==0:
        answer+=i

if answer==num:
    print("True")
else:
    print("False")