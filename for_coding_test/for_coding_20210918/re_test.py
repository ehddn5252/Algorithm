import re



a = re.search("\w{2}","staAABa")
b = re.findall("[A-Za-z]{2}","staAABa")
print(b)

#print(a)
#print(len(a[0]))
#print(len(b[0]))