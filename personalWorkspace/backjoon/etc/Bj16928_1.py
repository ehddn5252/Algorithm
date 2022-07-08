m, s = map(int, input().split(" "))
dp = [100 for _ in range(107)]
print(0)
ladders_key = []
ladders_value = []
snake_key = []
snake_value = []

for i in range(2,7):
    dp[i]=1
dp[0]=0
dp[1]=0
for _ in range(m):
    a,b = map(int,input().split(" "))
    ladders_key.append(a)
    ladders_value.append(b)

for _ in range(s):
    a,b = map(int,input().split(" "))
    snake_key.append(a)
    snake_value.append(b)
location = 1
while True:

    for dice in range(1, 7):
        for ladder_i, ladder in enumerate(ladders_key):
            if location+dice == ladder and dp[ladders_value[ladder_i]] > dp[location]+1:
                dp[ladders_value[ladder_i]] = dp[location]+1

        for snake_i, snake in enumerate(snake_key):
            if location+dice == snake and dp[snake_value[snake_i]]>dp[location]+1:
                dp[ladders_value[ladder_i]] = dp[location] + 1

        if (location+dice not in snake_key) and (location+dice not in ladders_key):
            if dp[location+dice]>dp[location]+1:
                dp[location + dice]=dp[location]+1


    location += 1
    if location==100:
        break


print(str(dp[100]).strip())