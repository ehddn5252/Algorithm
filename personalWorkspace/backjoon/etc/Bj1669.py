
# 멍멍이 쓰다듬기
#규칙이 int(sqrt(diff) *2) 으로 나타난다.


import math
x, y = map(int, input().split(" "));

diff = y-x
if diff==0:
    print(0)
elif math.sqrt(diff) == int((math.sqrt(diff))):
    print(int(math.sqrt(diff)*2)-1)
else:
    print(int(math.sqrt(diff)*2))

