n = int(input())
l=[]
for i in range(n):
    num = int(input())
    l.append(num)
# 등차
if l[1]-l[0] == l[2]-l[1]:
    print(l[-1]+l[1]-l[0])
elif l[1]/l[0]==l[2]/l[1]:
    print(int(l[1]/l[0]*l[-1]))