


def fib(n):
    global first_count

    if n == 1 or n == 2:
        first_count += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global second_count
    dp = [0 for i in range(41)]
    dp[0] = dp[1] = 1
    for i in range(3, n+1):
        second_count+=1
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

first_count = 0
second_count = 0
n = int(input())
fib(n)
print(first_count)
fibonacci(n)
print(second_count)
