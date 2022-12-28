t = int(input())
dp = [1 for i in range(t)]
numbers = list(map(int,input().split(" ")))
for i in range(t):
    for j in range(i):
        if numbers[j]>numbers[i]:
            dp[i] = max(dp[j]+1,dp[i])

print(max(dp))