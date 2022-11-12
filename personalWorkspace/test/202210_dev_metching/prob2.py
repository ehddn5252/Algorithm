from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
all_d: dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
               'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}


def DFS(i, j, maps, visit):
    global all_d
    d: dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
               'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    d[maps[i][j]] += 1
    stack = [[i, j]]
    while stack:
        popped = stack.pop()
        for i in range(4):
            new_i = popped[0] + dx[i]
            new_j = popped[1] + dy[i]

            if new_i >= 0 and new_i < len(maps) and new_j >= 0 and new_j < len(maps[0]):
                if maps[new_i][new_j] != '.' and visit[new_i][new_j] != 1:
                    d[maps[new_i][new_j]] += 1
                    visit[new_i][new_j] = 1
                    stack.append([new_i, new_j])

    max_value = max(d.values())
    max_alphabet = ""
    for key, value in d.items():
        if value is max_value:
            max_alphabet = key
    for key, value in d.items():
        if value < max_value:
            d[max_alphabet] += value
            d[key] = 0

    for key, value in d.items():
        all_d[key] += d[key]


def solution(maps):
    visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != '.' and visit[i][j] == 0:
                visit[i][j] = 1
                DFS(i, j, maps, visit)

    return max(all_d.values())
