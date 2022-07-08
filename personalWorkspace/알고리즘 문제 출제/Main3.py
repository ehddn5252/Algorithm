# 그리디
days, M = map(int, input().split(" "))

before_day = int(input())
before_before_day = int(input())
go_out_stack = 0
ans = 0
dp = []
for i in range(2, days):
    today = int(input())
    if(before_before_day == 0 and before_day == 0 or today == 0 or go_out_stack >= M):
        go_out_stack = 0
    else:
        go_out_stack += 1
        ans += 1
    before_before_day = before_day
    before_day = today

print(ans)