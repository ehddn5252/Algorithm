dp = [0 for _ in range(10001)]

testcase = int(input())

import math
def calc(n):
    ans = 0
    start = 3
    while n >= 0:
        ans += math.floor(n // 2) + 1
        n -= start
    return ans

for i in range(1, 10001):
    dp[i] =calc(i)


for _ in range(testcase):
    print(dp[int(input())])
