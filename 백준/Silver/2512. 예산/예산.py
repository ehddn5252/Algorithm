N = int(input())
l = list(map(int, input().split(" ")))
M = int(input())

l  .sort()

total = M
list_size = len(l)
avg = total / list_size
ans = 0
for i in range(len(l)):
    avg = total / list_size
    if l[i] <= avg:
        total -= l[i]
        list_size -= 1
        ans = l[i]
    else:
        ans=int(avg)
        break

print(ans)