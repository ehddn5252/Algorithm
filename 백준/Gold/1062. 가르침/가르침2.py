from itertools import combinations

N, K = map(int, input().split(" "))
l = []
# a n t c i 는 읽을 수 있어야 함 최소 5
simul_map = {'a': 1, 'n': 1, 'c': 1, 't': 1, 'i': 1}

alphabets = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w',
             'x', 'y', 'z']
for i in range(N):
    word = input()
    l.append(word)
max_ans=0
if K < 5:
    pass
else:
    K -= 5
    for i in combinations(alphabets, K):
        ans = len(l)
        for j in i:
            simul_map[j] = 1
        for j in range(len(l)):
            for k in l[j]:
                if simul_map.get(k) != 1:
                    ans -= 1
                    break
        if max_ans<ans:
            max_ans=ans
        for j in i:
            simul_map[j] = 0
print(max_ans)
