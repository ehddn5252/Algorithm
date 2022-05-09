from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1sum = sum(q1)
    q2sum = sum(q2)

    # queue 구현 완료
    # 넣기
    count = 0
    while (True):
        if (count > 10000000):
            return -1
        if q1sum > q2sum:
            q1pop = q1.popleft()
            q1sum -= q1pop
            q2sum += q1pop
            q2.append(q1pop)
            count += 1
        elif q1sum < q2sum:
            q2pop = q2.popleft()
            q2sum -= q2pop
            q1sum += q2pop

            q1.append(q2pop)
            count += 1
        else:
            return count

    return -1


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

solution(queue1,queue2)