from collections import deque

num = int(input())
visit = [[0 for i in range(1001)] for _ in range(1001)]
q = deque([[1, 0, 0]])

while q:
    popped = q.popleft()
    window = popped[0]
    clipboard = popped[1]
    time = popped[2]
    if window == num:
        print(time)
        break

    # 클립보드에 복사
    tmp = clipboard
    clipboard = window
    if window<=1000 and clipboard<=1000 and window>=0 and clipboard>=0 and not visit[window][clipboard]:
        visit[window][clipboard]=True
        q.append([window, clipboard, time + 1])
    clipboard = tmp

    # 이모티콘 제거
    window -= 1
    if window >= 0 and not visit[window][clipboard]:
        visit[window][clipboard]=True
        q.append([window, clipboard, time + 1])
    window += 1

    # 바탕화면에 복사
    window += clipboard
    if window <= 1000 and not visit[window][clipboard]:
        visit[window][clipboard]=True
        q.append([window, clipboard, time + 1])
    window -= clipboard

