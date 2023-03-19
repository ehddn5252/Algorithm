N, M = map(int, input().split(" "))

l = list(map(int, input().split(" ")))
players = [0 for _ in range(N)]
break_flag = False
for i in range(len(l)):
    players[(i + 1) % N] += l[i]

winner = max(players)
players.append(players.pop(0))
for i in range(len(players)-1,-1,-1):
    if players[i] == winner:
        print(i+1)
        break