N = int(input())
l = []

for i in range(N):
    l.append(int(input()))


def avg_f(l):
    print(int(round(sum(l) / N, 0)))


def middle(l):
    l.sort()
    sizes = len(l) // 2
    print(l[sizes])


def most_f(l):
    count_l = [0 for _ in range(8001)]
    for i in l:
        count_l[4000+i] += 1
    max_count = max(count_l)
    tmp = 0
    ans = 0
    count1 = 0
    for i in range(8001):
        if max_count == count_l[i]:
            ans = i
            count1+=1
        if count1==2:
            break
    print(ans-4000)


def rang(l):
    print(max(l) - min(l))


avg_f(l)
middle(l)
most_f(l)
rang(l)
