def rotate():
    global container, robots
    tmp = container[-1]
    for i in range(len(container) - 1, 0, -1):
        container[i] = container[i - 1]
    container[0] = tmp

    tmp = robots[N * 2 - 1]
    for i in range(N * 2 - 1, 0, -1):
        robots[i] = robots[i - 1]
    robots[0] = tmp
    if robots[N - 1] == 1:
        robots[N - 1] = 0


def move_robot():
    global container, robots
    # 초기
    if container[0] >= 1 and robots[0] == 0 and robots[-1] == 1:
        container[0] -= 1
        robots[0] = 1
        robots[-1] = 0

    for i in range(N * 2 - 2, -1, -1):
        if robots[i] == 1 and robots[i + 1] == 0:
            if container[i + 1] >= 1:
                container[i + 1] -= 1
                robots[i] = 0
                robots[i + 1] = 1
        if robots[N - 1] == 1:
            robots[N - 1] = 0


def upload_robot():
    global container, robots
    if container[0] >= 1:
        robots[0] = 1
        container[0] -= 1


def check_shield():
    global container
    if container.count(0) >= K:
        return True
    return False


def solve():
    time = 0
    while True:
        time += 1
        rotate()
        move_robot()
        upload_robot()
        if check_shield():
            break
    print(time)


if __name__ == "__main__":
    N, K = map(int, input().split(" "))

    container = list(map(int, input().split(" ")))
    robots = [0 for _ in range(N * 2)]
    solve()
