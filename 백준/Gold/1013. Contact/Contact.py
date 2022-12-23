import re
num = int(input())
for i in range(num):
    sign = input()
    pattern = "(100+1+|01)+"
    if re.fullmatch(pattern,sign):
        print("YES")
    else:
        print("NO")