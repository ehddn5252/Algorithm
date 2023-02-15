N, K = map(int, input().split(" "))

l = input()

'''
1. 2포인터로 완전 탐색한다.
'''
ans = 0
position = 0
visit = [False for _ in range(N)]
while position < N:
    if l[position] == 'H' and not visit[position]:
        visit[position] = True
        for i in range(1 + position, min(N,position + K + 1)):
            if l[i] == 'P' and not visit[i]:
                visit[i] = True
                ans += 1
                break
    elif l[position] == 'P' and not visit[position]:
        visit[position] = True
        for i in range(1 + position, min(N,position + K + 1)):
            if l[i] == 'H' and not visit[i]:
                visit[i] = True
                ans += 1
                break
    position += 1
print(ans)