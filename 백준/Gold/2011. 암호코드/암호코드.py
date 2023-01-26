input_str: str = input()

def solution(input_str):
    if input_str[0] == '0':
        return 0

    dp = [0 for _ in range(len(input_str) + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(input_str) + 1):
        if input_str[i - 1] != '0':
            dp[i] = dp[i - 1] % 1000000
        if 26 >= int(input_str[i - 2:i]) >= 10:
            dp[i] = (dp[i] + dp[i - 2]) % 1000000
    return dp[-1]

print(solution(input_str))
