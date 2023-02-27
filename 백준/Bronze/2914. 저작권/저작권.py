A, B = map(int, input().split(" "))
import math

ans = A*B-A-1

for i in range(ans, ans*2):
    if math.ceil((i / A)) == B:
        print(i)
        break
