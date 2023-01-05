visit = [False for i in range(26)]
visit[ord('a') - (ord('a'))] = True
visit[ord('n') - (ord('a'))] = True
visit[ord('t') - (ord('a'))] = True
visit[ord('i') - (ord('a'))] = True
visit[ord('c') - (ord('a'))] = True

n, m = map(int, input().split(" "))
l = [input() for i in range(n)]

max_num = 0


def dfs(start, count):
    global max_num, l, m
    if count == m:
        num = 0
        for word in l:
            answer_flag = True
            for alphabet in word:
                if not visit[ord(alphabet) - ord('a')]:
                    answer_flag = False
                    break
            if answer_flag:
                num += 1
        max_num = max(max_num, num)
        return

    for alphabet in range(start, 26):
        if not visit[alphabet]:
            visit[alphabet] = True
            dfs(alphabet, count + 1)
            visit[alphabet] = False


m = m - 5
if m < 0:
    print(0)
else:
    dfs(0, 0)
    print(max_num)
