N, C = map(int, input().split(" "))  # 집의 개수, 공유기 개수
import sys

l = []
for _ in range(N):
    l.append(int(sys.stdin.readline()))

l.sort()
start, end = 0, l[-1] - l[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    before_house = l[0]
    # 일정 거리에 하나씩 두면 되는 지 check
    for i in range(1, len(l)):
        if l[i] - before_house >= mid:
            cnt += 1
            before_house = l[i]

    if cnt >= C:
        ans = max(ans,mid)
        start = mid + 1

    else:
        end = mid - 1

print(ans)