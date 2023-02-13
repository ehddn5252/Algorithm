testcase = int(input())

for _ in range(testcase):
    player_num = int(input())
    l = list(map(int, input().split(" ")))
    player_map = {}
    for i in range(len(l)):
        player_map.setdefault(l[i], 0)
        player_map[l[i]] += 1
    pop_l = []
    for k, v in player_map.items():
        if v < 6:
            pop_l.append(k)
        else:
            player_map[k] = 0
    for k in list(player_map.keys())[::-1]:
        if player_map[k] != 0:
            player_map.pop(k)

    for i in range(len(pop_l)):
        for j in range(len(l) - 1, -1, -1):
            if l[j] == pop_l[i]:
                l.pop(j)

    player_score_map = {}
    player5_score_list = []
    for i in range(len(l)):
        if player_map[l[i]] < 4:
            player_score_map.setdefault(l[i], 0)
            player_score_map[l[i]] += i + 1  # 1점부터 시작함
            player_map[l[i]] += 1
        elif player_map[l[i]] == 4:
            player5_score_list.append(l[i])
            player_map[l[i]] += 1
    ans = 0
    calc_min_scores = [k for k, v in player_score_map.items() if min(player_score_map.values()) == v]
    if len(calc_min_scores) > 1:
        for player in player5_score_list:
            if player in calc_min_scores:
                ans = player
                break
    else:
        ans = calc_min_scores[0]
    print(ans)
