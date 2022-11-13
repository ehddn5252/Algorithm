from itertools import combinations

start_index = 0
while True:
    lotto = list(map(int, input().split(" ")))
    if lotto[0] == 0:
        break
    lotto = lotto[1:]
    if start_index != 0:
        print()

    for i in combinations(lotto, 6):
        s = ""
        for j in i:
            s += str(j) + " "
        print(s.strip())
    start_index +=1