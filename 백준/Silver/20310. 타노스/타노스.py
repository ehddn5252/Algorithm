from collections import deque

str1 = list(map(str, input()))

will_remove_zero_cnt = str1.count('0') // 2
will_remove_one_cnt = str1.count('1') // 2
start = 0
while will_remove_one_cnt > 0:
    if str1[start] == '1':
        will_remove_one_cnt -= 1
        str1.pop(start)
    else:
        start += 1

end = len(str1) - 1
while will_remove_zero_cnt > 0:
    if str1[end] == '0':
        str1.pop(end)
        will_remove_zero_cnt -= 1
    end -= 1
t = "".join([s for s in str1])
print(t)