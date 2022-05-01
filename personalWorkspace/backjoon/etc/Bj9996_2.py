import re

l = re.fullmatch("a.*d","abcd")
print(l.group(0))
