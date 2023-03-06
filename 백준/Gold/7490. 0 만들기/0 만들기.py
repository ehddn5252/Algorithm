testcase = int(input())

def dfs(now, l):
    global ans_l
    if now == n:
        start = "1"
        for i in range(2, n + 1):
            start += l[i - 2]
            start += str(i)
        new_start = start.replace(" ", "")
        result = eval(new_start)
        if result == 0:
            ans_l.append(start)
        return
    l.append("+")
    dfs(now + 1, l)
    l.pop()
    l.append(" ")
    dfs(now + 1, l)
    l.pop()
    l.append("-")
    dfs(now + 1, l)
    l.pop()


for tc in range(testcase):
    ans_l = []
    n = int(input())
    dfs(1, [])
    ans_l.sort()
    for calc in ans_l:
        print(calc)
    print()
