import math

def calc(x,y,cx,cy,r):
    if math.sqrt(abs(x-cx)**2+abs(y-cy)**2)<r:
        return True
    else:
        return False

testcase = int(input())


for _ in range(testcase):
    x1, y1, x2, y2 = map(int, input().split(" "))
    ans=0
    n = int(input())
    for i in range(n):
        cx, cy, r = map(int, input().split(" "))
        c1 = calc(x1, y1, cx, cy, r)
        c2 = calc(x2,y2,cx,cy,r)
        if c1 and not c2 or (c2 and not c1):
            ans += 1
    print(ans)