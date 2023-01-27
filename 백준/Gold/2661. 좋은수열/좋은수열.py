def check(l):
    if len(l) == 1 or len(l) == 0:
        return True
    mid = len(l) // 2
    if len(l) % 2 == 1:
        for i in range(mid):
            if l[mid + i + 1] != l[i + 1]:
                return check(l[3:])
    else:
        for i in range(mid):
            if l[mid + i] != l[i]:
                return check(l[2:])
    return False


n = int(input())
nums = (1, 2, 3)
ans = []

return_flag = False


def dfs(l):
    global ans, return_flag
    if return_flag:
        return
    if len(l) == n:
        ans = l.copy()
        return_flag = True
        return
    for num in nums:
        l.append(num)
        if check(l):
            dfs(l)
        l.pop()


dfs([1])

ans_str = ""
for i in range(len(ans)):
    ans_str += str(ans[i])
print(ans_str)
