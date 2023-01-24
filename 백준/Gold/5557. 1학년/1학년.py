n = int(input())

l = list(map(int, input().split(" ")))
'''
1. 수를 더하면 0 이상 20 이하가 되어야 한다.
2. 맨 처음 숫자의 부호는 + 이다.

'''
dp = [{} for _ in range(n)]

dp[0][l[0]] = 1
for i in range(1, n - 1):
    for key in dp[i - 1].keys():
        if 0 <= key + l[i] <= 20:
            dp[i].setdefault(key + l[i], 0)
            dp[i][key + l[i]] += dp[i - 1][key]
        if 20 >= key - l[i] >= 0:
            dp[i].setdefault(key - l[i], 0)
            dp[i][key - l[i]] += dp[i - 1][key]

print(dp[-2][l[-1]])