def f(num):
    global t
    sum=0
    for i in range(num):
        sum+=t[i]*t[num-i-1]
    t.append(sum)
t=[1]
for i in range(1,36):
    f(i)
i = int(input())
print(t[i])
