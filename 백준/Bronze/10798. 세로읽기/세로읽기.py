l = []
m = 0
for i in range(5):
    l.append(input())

ans = ''
start = 0
for j in range(15):
    for i in range(5):
        if len(l[i])>j:
            ans+=l[i][j]
    start+=1
print(ans)