"""
1. 플레이어가 처음 들어올 때, 방을 생성한다.
2. 만약 그 플레이어 레벨의 +10 보다 높거나 -10보다 낮으면 다른 방을 추가한다.

"""

p, m = map(int, input().split(" "))  # 플레이어 수, 방의 정원
room = []

for i in range(p):
    # 플레이어의 레벨과 닉네임
    level, name = map(str, input().split(" "))
    level = int(level)
    break_flag = False
    for j in range(len(room)):
        if len(room[j]) == m:
            continue
        if room[j][0][0] - 10 <= level <= room[j][0][0] + 10:
            room[j].append([level, name])
            break_flag = True
            break
    if not break_flag:
        room.append([[level, name]])

for i in range(len(room)):
    if len(room[i]) < m:
        print("Waiting!")
    else:
        print("Started!")
    room[i].sort(key=lambda x: x[1])
    for level, nick in room[i]:
        print(level, nick)