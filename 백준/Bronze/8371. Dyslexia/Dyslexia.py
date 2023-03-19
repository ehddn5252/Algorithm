n = int(input())
n1 = input()
n2 = input()
ans = 0
for i in range(n):
    if n1[i] != n2[i]:
        ans += 1

print(ans)