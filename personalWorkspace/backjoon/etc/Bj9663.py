N = int(input())
rows = [0 for i in range(N)]
ans = 0

def is_promising(row_index):
    for i in range(row_index):
        # 같은 row or 대각선 일치하면 false
        if (rows[row_index] == rows[i] or abs(rows[row_index] - rows[i]) == (row_index - i)):
            return False
    return True

def DFS(row_index):
    global ans
    if row_index == N:
        ans += 1
        return

    for i in range(N):
        rows[row_index] = i
        if is_promising(row_index):
            DFS(row_index + 1)

DFS(0)
print(ans)
