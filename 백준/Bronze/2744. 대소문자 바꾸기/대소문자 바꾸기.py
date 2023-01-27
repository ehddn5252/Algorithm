l = input()
ans = ""
for i in l:
    if ord(i)<97:
        ans+=chr(ord(i)+32)
    else:
        ans+=chr(ord(i)-32)
print(ans)