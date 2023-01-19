# 총 N명 중 p명에게 줌 E개 러버덕 인형,
N, P, E = map(int, input().split(" "))
l = []
for i in range(N):
    # 회원은 x개 이상 y개 이하 받음
    tmp = list(map(int, input().split(" ")))
    tmp.append(i)
    l.append(tmp)
ans = []
from itertools import combinations

for selected in combinations(l, P):
    start = 0
    end = 0
    for i in selected:
        start += i[0]
        end += i[1]
    if start <= E <= end:
        ans = list(selected)
        break
if ans == []:
    print(-1)
else:
    ssss = 0
    ans.sort(key=lambda x: x[0])
    divied = E // P
    ans_l = [0 for i in range(N)]
    for i, v in enumerate(ans):
        if v[0] > divied:
            ans_l[v[2]] = v[0]
            ssss += v[0]
        elif v[0] <= divied <= v[1]:
            ans_l[v[2]] = divied
            ssss += divied

        elif v[1] < divied:
            ans_l[v[2]] = v[1]
            ssss += v[1]
    while ssss != E:
        for i, v in enumerate(ans):
            if ssss > E:
                if v[0] <= ans_l[v[2]] -1 <= v[1]:
                    ans_l[v[2]] -= 1
                    ssss -= 1
            elif ssss < E:
                if v[0] <= ans_l[v[2]] + 1 <= v[1]:
                    ans_l[v[2]] += 1
                    ssss += 1

    print(" ".join(str(tt) for tt in ans_l))