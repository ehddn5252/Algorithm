n = int(input())

l = list(map(int, input().split(" ")))

answers = [10000 for i in range(n)]
time = 0
no_count=0
while no_count<=1000:
    for i, v in enumerate(l):
        if l[i] == 0:
            no_count+=1
            continue
        else:
            no_count=0
            l[i]-=1
            time+=1
            if l[i] == 0:
                answers[i] = str(time)
print(" ".join(answers))