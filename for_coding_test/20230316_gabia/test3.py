import heapq


def solution(N, coffee_times):
    answer = []
    making = []
    now = 0
    time = 0
    full=False
    while True:
        if now < len(coffee_times):
            while len(making) < N:
                if now == len(coffee_times):
                    break
                heapq.heappush(making, [coffee_times[now] + time, now])
                now += 1

        if not making:
            break
        before = -1
        if not full:
            time += 1
        while making:
            popped = heapq.heappop(making)
            if before != -1:
                if popped[0] != before:
                    heapq.heappush(making, popped)
                    break
                else:
                    answer.append(popped[1] + 1)
                    continue
            before = popped[0]
            if popped[0] > time:
                heapq.heappush(making, popped)
                if len(making)==N:
                    time=popped[0]
                    full=True
                else:
                    full=False
                break
            else:
                answer.append(popped[1] + 1)

    return answer
