n = int(input())
l = list(map(int, input().split(" ")))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if l[i]<l[j]:
            dp[j]=max(dp[j],dp[i]+1)

print(max(dp))