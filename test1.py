D, F = map(int, input().split())
M = 3
friend = list(map(int, input().split()))
dp = [[0] * 5 for _ in range(M)]    # 날짜정보, 외출여부, No외출, 하루외출, 연속외출
                                    # 0이면 안나감 / 1이면 자율 / 2이면 무조건 나감
dp[0][0] = dp[0][1] = dp[1][1] = dp[1][0] = 1
dpIdx = 2

for i in range(D):
    dp[dpIdx][0] = int(input())
    for j in range(F):
        if friend[j] - 1 == i:
            dp[dpIdx][1] = 2
            dp[dpIdx][3] = dp[(dpIdx + 2) % M][2] + 1 if dp[(dpIdx + 2) % M][1] != 2 else 0
            dp[dpIdx][4] = dp[(dpIdx + 2) % M][3] + 1 if dp[(dpIdx + 2) % M][1] != 0 else 0
            dpIdx = (dpIdx + 1) % M
            break
            # continue=======================================================================
    if dp[dpIdx][0] == 0 or dp[(dpIdx + 2) % M][0] == 0 and dp[(dpIdx + 1) % M][0] == 0:
        dp[dpIdx][1] = 0
        dp[dpIdx][2] = max(dp[(dpIdx + 2) % M][2], dp[(dpIdx + 2) % M][3], dp[(dpIdx + 2) % M][4])
    else:
        dp[dpIdx][1] = 1
        dp[dpIdx][3] = dp[(dpIdx + 2) % M][2] + 1 if dp[(dpIdx + 2) % M][1] != 2 else 0
        dp[dpIdx][4] = dp[(dpIdx + 2) % M][3] + 1 if dp[(dpIdx + 2) % M][1] != 0 else 0
        dp[dpIdx][2] = max(dp[(dpIdx + 2) % M][2], dp[(dpIdx + 2) % M][3], dp[(dpIdx + 2) % M][4])
    dpIdx = (dpIdx + 1) % M

print(max(dp[(dpIdx + 2) % M][2], dp[(dpIdx + 2) % M][3], dp[(dpIdx + 2) % M][4]))