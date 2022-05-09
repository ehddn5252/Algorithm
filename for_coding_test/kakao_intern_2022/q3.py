from collections import deque


max_alp = 0
max_cop = 0
ans = 9876543210


def solution(alp, cop, problems):
    # dp로 모든 경우를 구하면 될 듯 근데 안해도 되고 중복가능해서 흠..
    # BFS 나 DFS 를 생각해보자.
    # 일단 max 값을 얻어야 한다.
    global max_alp, max_cop, ans
    for i, problem in enumerate(problems):
        if max_alp < problem[0]:
            max_alp = problem[0]

        if max_cop < problem[1]:
            max_cop = problem[1]

    bfs(problems, alp, cop, 0)

    return ans


def bfs(problems, alp, cop, cost):
    global max_alp, max_cop, ans
    q = deque([[alp, cop, cost]])
    count = 0
    while(q):
        count+=1
        if count==1000000:
            return ans
        popped = q.pop()
        if popped[0]>= max_alp and popped[1] >= max_cop:
            if popped[2] < ans:
                ans = popped[2]
            continue
        # 현재 풀수 있고 최고의 성능을 내는 문제만 나둔다.

        for problem in problems:
            if problem[0] <= popped[0] and problem[1] <= popped[1]:
                if(popped[0]>=max_alp and problem[3]==0):
                    continue
                if(popped[1]>=max_cop and problem[2]==0):
                    continue
                q.append([popped[0] + problem[2], popped[1] + problem[3], popped[2] + problem[4]])

            elif problem[0] > popped[0] and problem[1] <= popped[1]:
                q.append([problem[0], popped[1], popped[2] + problem[0] - popped[0]])

            elif problem[0] <= popped[0] and problem[1] > popped[1]:
                q.append([popped[0], problem[1], popped[2] + problem[1] - popped[1]])

            elif problem[0] > popped[0] and problem[1] > popped[1]:
                q.append([problem[0], problem[1], popped[2] + problem[1] - popped[1] + problem[0] - popped[0]])
