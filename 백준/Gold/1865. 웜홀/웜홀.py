import sys


def floyd(l, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if l[i][j] > l[i][k] + l[k][j]:
                    l[i][j] = l[i][k] + l[k][j]
                if i == j and l[i][j] < 0:
                    return "YES"
    return "NO"


testcase = int(sys.stdin.readline())
INF = 9999999

for _ in range(testcase):
    N, M, W = map(int, sys.stdin.readline().split(" "))
    l = [[0 if i == j else INF for j in range(N)] for i in range(N)]

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split(" "))
        S = S - 1
        E = E - 1
        if l[S][E] > T or l[S][E] > T:
            l[S][E] = T
            l[E][S] = T

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split(" "))
        S = S - 1
        E = E - 1
        l[S][E] = -T
    sys.stdout.write(floyd(l, N) + '\n')
