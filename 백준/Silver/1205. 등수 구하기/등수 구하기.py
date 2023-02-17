N, new_score, P = map(int, input().split(" "))
if N==0:
    print(1)
else:
    l = sorted(list(map(int, input().split(" "))), reverse=True)

    rank_list = []

    import heapq

    for i in range(len(l)):
        if len(rank_list) < P:
            heapq.heappush(rank_list,l[i])
        else:
            popped = heapq.heappop(rank_list)
            if popped > l[i]:
                heapq.heappush(rank_list, popped)
            else:
                heapq.heappush(rank_list, l[i])

    while rank_list:
        popped = heapq.heappop(rank_list)
        if popped > new_score:
            if len(rank_list) + 1 >= P:
                print(-1)
                exit(0)
            rank_list.append(popped)
            break
        elif popped < new_score:
            continue
        elif popped == new_score:
            if len(rank_list) + 1 >= P:
                print(-1)
                exit(0)
            else:
                continue
    print(len(rank_list) + 1)
