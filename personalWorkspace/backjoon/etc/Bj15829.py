#

import sys
num = sys.stdin.readline()
s = sys.stdin.readline()
s = s[:-1]
dict1 = {}
ASCII_A_MINUS_1 = 97 - 1
R = 31
M = 1234567891
ans = 0
for i,v in enumerate(s):
    ans+= 31**i *(ord(v)-ASCII_A_MINUS_1)

print(ans % M)


