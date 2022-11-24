"""
요구 사항
1. 연결된 컴퓨터 수 확인하기.

방법
1. visit 을 확인해서 queue 에 넣는다. -> DFS
2.

"""


def solution(n, computers):
    visit = [0 for _ in range(n)]
    return dfs(computers, visit)


def dfs(computers, visit):
    now_index = 0
    queue = []
    for i, v in enumerate(computers):
        if visit[i] == 0:
            now_index += 1
            queue.append(i)
            while queue:
                popped = queue.pop(0)
                for c_i, c_v in enumerate(computers[popped]):
                    if visit[c_i] == 0 and c_v == 1:
                        visit[c_i] = now_index
                        queue.append(c_i)
    return max(visit)
