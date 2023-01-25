N = int(input())
first = list(map(int, input().split(" ")))
maxes = first[:]
mins = first[:]
for _ in range(N - 1):
    now = list(map(int, input().split(" ")))
    before_max1 = maxes[0]
    before_max2 = maxes[1]
    before_max3 = maxes[2]

    before_min1 = mins[0]
    before_min2 = mins[1]
    before_min3 = mins[2]

    for j in range(3):
        if j == 0:
            maxes[j] = max(before_max1,before_max2) + now[0]
            mins[j] = min(before_min1,before_min2) + now[0]
        elif j == 1:
            maxes[j] = max(before_max1,before_max2,before_max3) + now[1]
            mins[j] = min(before_min1,before_min2,before_min3) + now[1]

        elif j == 2:
            maxes[j] = max(before_max3,before_max2) + now[2]
            mins[j] = min(before_min3,before_min2) + now[2]
print(max(maxes), min(mins))
