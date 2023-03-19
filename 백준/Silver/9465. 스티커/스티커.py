testcase_num = int(input())

for _ in range(testcase_num):
    col_size = int(input())
    dp = [ list(map(int, input().split(" "))) for _ in range(2)]
    if len(dp[0]) == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        dp[0][1] = dp[0][1]+dp[1][0]
        dp[1][1] = dp[1][1]+dp[0][0]
        for j in range(2, col_size):
            dp[0][j] = max(dp[0][j] + dp[1][j-1], dp[0][j]+dp[1][j-2])
            dp[1][j] = max(dp[1][j] + dp[0][j-1], dp[1][j]+dp[0][j-2])

        print(max(dp[0][col_size-1], dp[1][col_size-1]))