import math

N = int(input())

dp = [ 4 for i in range(50001)]
MAX_VALUE =int(math.sqrt(N))+1

for i in range(1,224+1):
    val = i**2
    if i**2 > 50000:
        break
    dp[val] = 1

for i in range(1, MAX_VALUE+1):
    i_2 = i**2
    for j in range(i, MAX_VALUE+1):
        j_2 = j**2
        if i_2+j_2 > 50000:
            break
        dp[i_2+j_2] = min(2, dp[i_2+j_2])

for i in range(1, MAX_VALUE+1):
    i_2 = i**2
    for j in range(i, MAX_VALUE+1):
        i_j_2 = i_2 + j**2
        for k in range(j, MAX_VALUE+1):
            k_2 = k**2
            if i_j_2+k_2>50000:
                break
            dp[i_j_2+k_2] = min(dp[i_j_2+k_2], 3)

print(dp[N])