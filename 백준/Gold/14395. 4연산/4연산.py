s, t = map(int, input().split(" "))

dl = ['*', '+', '/']
ans_list = []
from collections import deque

ans = 0
q = deque([[s, ""]])
map1 = {s: True}
visit = [False for _ in range(10000000)]
if s == t:
    print(0)
else:
    while q:
        num, str1 = q.popleft()
        if num > 1000000000:
            continue

        if num == t:
            ans_list.append(str1)

        for i in range(len(dl)):
            if dl[i] == '*' and not map1.get(num * num):
                map1[num * num] = True
                q.append([num * num, str1 + dl[i]])
            elif dl[i] == '+' and not map1.get(num + num):
                map1[num + num] = True
                q.append([num + num, str1 + dl[i]])
            elif dl[i] == '/' and not map1.get(num // num):
                map1[num // num] = True
                q.append([num // num, str1 + dl[i]])
    if len(ans_list) != 0:
        ans_list.sort()
        print(ans_list[0])
    else:
        print(-1)
