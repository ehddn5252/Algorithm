from collections import deque

testcase = int(input())
for _ in range(testcase):
    commands = input()
    pointer = "L"
    n = int(input())
    error_flag=False
    if n != 0:
        l = deque(input()[1:-1].split(","))
    else:
        input()
        l = deque([])
    for command in commands:
        if command == "R":
            if pointer == "L":
                pointer = "R"
            else:
                pointer = "L"
        elif command == "D":
            if len(l) == 0:
                print("error")
                error_flag=True
                break
            if pointer == "L":
                l.popleft()
            elif pointer == "R":
                l.pop()
    if len(l) != 0:
        if pointer == "R":
            l.reverse()
        print(f"[", end="")
        for i in range(len(l)):
            if i != len(l) - 1:
                print(l[i] + ",", end="")
            else:
                print(l[i] + "]")
    elif not error_flag:
        print("[]")