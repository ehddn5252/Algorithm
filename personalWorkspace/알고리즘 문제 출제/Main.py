from collections import deque

go_out_stack = 0
# 주어진 날짜
days = int(input())
# 연속으로 나가게 되면 지치게 되는 일수
M = int(input())
# 30+M 배열 만들기
count_list = deque([])
# 첫째날 하고 둘째날  init
count_list.append(int(input()))
count_list.append(int(input()))
# 정답
ans = 0
# 30일 기준으로 연속으로 나가는 count
day_count = 0

# 100,000,000
# 여기서 첫 날과 둘째 날에 나가는 경우를 확인 해야 한다.

before_list = deque([])
for i in range(2, days):
    if len(count_list) <= 30:
        count_list.append(int(input()))
    else:
        before_list.append(count_list.popleft())

        if(len(before_list)) > 2:
            before_list.popleft()
        count_list.append(int(input()))

    day_count = 0
    
    # 여기서 첫날과 두번째 날은 그전날과 전전날의 영향을 받는다. 그에 따라 day_count를 초기화 해준다.
    if(len(before_list)==2):
        if (before_list[-2] != 0 or before_list[-1] != 0 and count_list[0]==1):
            day_count += 1
        if before_list[-1] != 0 or count_list[0]!=0 and count_list[1]==1:
            day_count += 1

    elif len(before_list)==1:
        if before_list[-1] != 0 or count_list[0]!=0 and count_list[1]==1:
            day_count += 1

    for j in range(2, len(count_list)):
        # 안나가는 조건
        # 1. 당일에 흐리다.
        # 2. 전날과 전전날에 흐리다.
        # 3. M일연속으로 나가게 된다.
        if count_list[j]==0 or count_list[j-2] == 0 and count_list[j-1] == 0 or go_out_stack>=M:
            go_out_stack = 0
        else:
            go_out_stack += 1
            day_count += 1

    if day_count>=ans:
        ans = day_count

print(ans)
