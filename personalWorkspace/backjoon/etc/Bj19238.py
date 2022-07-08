from collections import deque
from pprint import pprint

# input and data setting
N, M, start_fuel = map(int, input().split(" "))
map1 = [list(map(int, input().split(" "))) for _ in range(N)]
client_visit = [0 for i in range(M)]
start_i, start_j = map(int, input().split(" "))
clients = []
exit_flag = False
for _ in range(M):
    client = list(map(int, input().split(" ")))
    # 인덱스는 0부터 시작하므로 모든 입력 값에 1을 빼준다
    for i in range(len(client)):
        client[i] -= 1
    clients.append(client)

# 인덱스는 0부터 시작하므로 모든 입력 값에 1을 빼준다
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
near_client = [0,0,0,0]
s = [[start_i - 1, start_j - 1, start_fuel]]
for count in range(M * 2):
    destination = 0
    visit = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque(s)
    fuel = start_fuel
    while q:
        popped = q.popleft()
        visit[popped[0]][popped[1]] = popped[2]
        if popped[2] == 0:
            continue
        for j in range(4):
            next_i = popped[0] + di[j]
            next_j = popped[1] + dj[j]
            if next_i >= 0 and next_i < N and next_j >= 0 and next_j < N and map1[next_i][next_j] != 1 and \
                    visit[next_i][next_j] < popped[2] - 1:
                visit[next_i][next_j] = popped[2] - 1
                q.append([next_i, next_j, popped[2] - 1])

    # count % 2 일때가 고객 찾으러 다닐 때이다.
    # 가장 가까운 고객 찾기
    if count % 2 == 0:
        # index, 연료, 행, 열
        near_client = [-1, -1, 9999, 9999]
        for i, client in enumerate(clients):
            if client_visit[i]==0:
                if visit[client[0]][client[1]] >= near_client[1]:
                    ## 남은 연료가 같으면 행, 열 낮은 순으로 비교한다.
                    if visit[client[0]][client[1]] == near_client[1]:

                        if near_client[2] == client[0]:
                            if near_client[3] < client[1]:
                                continue
                        elif near_client[2] < client[0]:
                            continue

                    near_client[0] = i
                    near_client[1] = visit[client[0]][client[1]]
                    near_client[2] = client[0]
                    near_client[3] = client[1]
    else:
        # 고객의 목적지 찾기
        for i in range(len(client_visit)):
            if client_visit[i] == 1:
                destination = i
                client_visit[i] = 2
                break
        near_client[1] = visit[clients[destination][2]][clients[destination][3]]

    if near_client[1] < 0:
        exit_flag=True
        break

    # 연료는 2배가 된다.
    # 고객 목적지에 도착한 경우
    if client_visit[near_client[0]] == 0:
        start_fuel = near_client[1]
        client_visit[near_client[0]] = 1
        s = [[clients[near_client[0]][0], clients[near_client[0]][1], start_fuel]]
    # 고객만 태운 경우
    else:
        start_fuel = near_client[1] + (fuel - near_client[1]) * 2
        s = [[clients[near_client[0]][2], clients[near_client[0]][3], start_fuel]]

if exit_flag:
    print(-1)
else:
    print(start_fuel)
