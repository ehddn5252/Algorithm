n = int(input())  # max 1,000,000

MOD = 1000000000

dp = [1 for _ in range(1000001)]

for i in range(2, len(dp)):
    if i % 2 == 1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i // 2] + dp[i -1]) %MOD

print(dp[n])