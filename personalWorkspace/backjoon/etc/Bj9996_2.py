import re

num = int(input())
pattern = input()
for i in range(num):
    s = input()
    print(pattern, s)
    l = re.fullmatch(pattern,s)
    print(l)
    if(l!=None):
        if(l.group(0)==s):
            print("DA")
    else:
        print("NE")