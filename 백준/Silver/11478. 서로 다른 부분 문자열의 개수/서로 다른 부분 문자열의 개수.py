str1 = input()
s = set([])
for i in range(len(str1)):
    for j in range(len(str1)):
        if j+i<len(str1):
            s.add(str1[j:j+i+1])
print(len(s))
