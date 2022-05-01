import sys
print= sys.stdout.write

def solution():
    N = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N):
        dp[i][i] = 1

    for i in range(N-1):
        if(l[i]==l[i+1]):
            dp[i][i+1] = 1

    for diff in range(2,N):
        for i in range(N-diff):
            if l[i]==l[i+diff] and dp[i+1][i+diff-1]==1:
                dp[i][i+diff]=1

    for i in range(M):
        start, end = map(int, sys.stdin.readline().split())
        print("%d\n" %dp[start-1][end-1])


if __name__ == "__main__":
    solution()
