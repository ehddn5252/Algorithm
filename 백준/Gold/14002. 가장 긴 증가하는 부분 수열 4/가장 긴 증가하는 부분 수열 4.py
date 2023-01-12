import sys
from collections import deque

N = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().strip().split()))

dp = [1] * len(number_list)
for i in range(len(number_list)):
    for j in range(i):
        if number_list[j] < number_list[i]:
            dp[i] = max(dp[j] + 1, dp[i])
max_value = max(dp)+1
max_index = dp.index(max_value-1)
ans_q = []
for i in range(max_index, -1, -1):
    if dp[i] == max_value-1:
        ans_q.append(number_list[i])
        max_value = dp[i]
print(max(dp))
print(" ".join(str(i) for i in sorted(ans_q)))
