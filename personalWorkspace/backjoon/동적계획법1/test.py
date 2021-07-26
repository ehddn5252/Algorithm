N = int(input())

dp = ["" for _ in range(1001)]
dp[1]="SK"
dp[2]="CY"
dp[3]="SK"
dp[4]="CY"
dp[5]="SK"
dp[6]="CY"

for i in range(5,1001):
    if dp[i-3]=="SK":
        dp[i]="CY"
    elif dp[i-3]=="CY":
        dp[i]="SK"

    if dp[i-1]=="SK":
        dp[i]="CY"
    elif dp[i-1]=="CY":
        dp[i]="SK"

print(dp[N])