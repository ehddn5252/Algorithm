N, K = map(int, input().split(" "))
l = []
for i in range(N):
    a, b, c, d = map(int, input().split(" "))
    l.append([b, c, d, a])

l.sort(key=lambda x: (-x[0], -x[1], -x[2]))
start = [l[0], l[1], l[2]]
rank = 1
answers = [rank, ]
ans_count = 1
for i in range(1, len(l)):
    if l[i][0] == start[0] and l[i][1] == start[1] and l[i][2] == start[2]:
        ans_count += 1
    else:
        start = l[i][:3]
        rank += ans_count
        ans_count = 1

    answers.append(rank)

for i,v in enumerate(l):
    if v[3]==K:
        print(answers[i])
        break