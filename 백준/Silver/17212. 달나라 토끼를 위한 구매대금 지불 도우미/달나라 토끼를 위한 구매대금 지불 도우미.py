n = int(input())

coins = 0
coin_cases = [7, 5, 2, 1]
if (n - 10) % 7 == 0 and n - 10 >= 0:
    coins = (n - 10) // 7 + 2
else:
    for coin_case in coin_cases:
        coins += n // coin_case
        n = n % coin_case

print(coins)