n = int(input())
l = list(map(int,input().split(" ")))
ans=0
for i in range(len(l)):
    if l[i]==n:
        ans+=1
print(ans)