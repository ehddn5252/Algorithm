from collections import deque

subin, bro = map(int, input().split(" "))

dist = [0 for _ in range(100001)]
move = [0 for _ in range(100001)]
ans = 100001
ans_route = []
MAX_LIMIT = 100000

q = deque([subin])

def print_path(x):
    arr = []
    now_location = x
    for i in range(dist[x]):
        arr.append(move[now_location])
        now_location = move[now_location]
    arr.reverse()
    arr.append(x)
    print(*arr)

while q:
    popped = q.popleft()
    current_loc = popped

    if current_loc == bro and ans > dist[current_loc]:
        ans = dist[current_loc]
        print(ans)
        print_path(current_loc)
        break

    for x in (current_loc + 1, current_loc * 2, current_loc - 1):
        if x >= 0 and x <= MAX_LIMIT and dist[x] == 0:
            q.append(x)
            dist[x] = dist[current_loc] + 1
            move[x] = current_loc