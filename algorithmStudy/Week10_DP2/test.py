#파이썬 1등
def s():
    s1, s2 = "ACAYKP","CAPCAK"

    dp = [0] * 10
    # 문자열 1
    for i in range(len(s1)):
        max_dp = 0
        #문자열2 
        for j in range(len(s2)):
            if max_dp < dp[j]:
                max_dp = dp[j]

            elif s1[i] == s2[j]:
                dp[j] = max_dp + 1
        print(dp)

    print(max(dp))
s()

