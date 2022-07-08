n = int(input())

stairs = [[0 for _ in range(10)] for _ in range(n)]
stairs[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i, stair in enumerate(stairs):
    if i == 0:
        continue

    stairs[i][0] = stairs[i - 1][1]
    stairs[i][9] = stairs[i - 1][8]
    for stair_num in range(1, 9):
        stairs[i][stair_num] = stairs[i - 1][stair_num - 1] + stairs[i - 1][stair_num + 1]

print(sum(stairs[n-1])%1000000000)
