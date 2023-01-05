# 부분 합 중 합이 S 이상이 되는 것 중 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오

N, S = map(int, input().split(" "))
l = list(map(int, input().split(" ")))

start, end = 0, 0
ans = 0
count = 0
INF = 9999999999
min_ans = INF
while start <= end <= N:
    if ans >= S:
        min_ans = min(min_ans, count)
        while start < end:
            ans -= l[start]
            start += 1
            count -= 1
            if ans < S:
                break
            else:
                min_ans = min(min_ans, count)
    elif ans < S:
        if end==N:
            break
        count+=1
        ans += l[end]
        end += 1

if min_ans==INF:
    print(0)
else:
    print(min_ans)
