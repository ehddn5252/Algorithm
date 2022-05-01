import re

def check_string(s):
    check_str = ""
    for i,v in enumerate(s):
        if v=='*':
            check_str+='.'
        check_str+=v
    return check_str

num = int(input())
pattern = input()

pattern=check_string(pattern)
for i in range(num):
    s = input()

    l = re.fullmatch(pattern,s)
    if(l!=None):
        print("DA")
    else:
        print("NE")