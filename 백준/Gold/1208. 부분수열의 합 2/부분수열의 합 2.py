import sys
sys.setrecursionlimit(100000)



N, S = map(int, input().split(" "))

l = list(map(int, input().split(" ")))

ans = 0
visit = [False for i in range(len(l))]

left_sums = []
right_sums = []
sums = {}

def left_get_sum(start, value):
    global ans
    if start == N // 2:
        sums.setdefault(S-value,0)
        ans+=sums[S-value]
        return

    left_get_sum(start + 1, value)
    left_get_sum(start + 1, value + l[start])


def right_get_sum(start, value):
    if start == N:
        sums.setdefault(value,0)
        sums[value]+=1
        return
    right_get_sum(start + 1, value)
    right_get_sum(start + 1, value + l[start])


right_get_sum(N // 2, 0)
left_get_sum(0, 0)
if S==0:
    print(ans-1)
else:
    print(ans)
