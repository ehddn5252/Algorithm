"""
1. max 값 이전에은 무조건 산다.
2. max 값에 다 판다.
3. 그 다음부터의 맥스 값을 산다.
"""
import sys

testcase = int(sys.stdin.readline())
for _ in range(testcase):
    sys.stdin.readline()
    l = list(map(int, sys.stdin.readline().split(" ")))
    now_max = l[-1]
    ans = 0
    cost = 0
    for i in range(len(l)-1,-1,-1):
        if now_max <= l[i]:
            now_max = l[i]
        else:
            ans += now_max - l[i]
    print(ans)