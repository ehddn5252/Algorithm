
l = list(map(int, input().split(" ")))
ans=""
t = [1,1,2,2,2,8]
for i in range(6):
    ans+=str(t[i]-l[i])+" "
print(ans[:-1])