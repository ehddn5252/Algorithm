n, k = int(input()), list(map(int, input().split()))
m, l = int(input()), list(map(int, input().split()))

# 추의 무게는 최대 500이므로 [[추의 개수*500]*추의 개수]로 배열을 구성한다.
dp, r = [[0 for j in range((i + 1) * 500 + 1)] for i in range(n + 1)], []


def cal(num, weight):
    if num > n:
        return

    if dp[num][weight]:
        return

    dp[num][weight] = 1

    cal(num + 1, weight)
    cal(num + 1, weight + k[num - 1])
    cal(num + 1, abs(weight - k[num - 1]))


cal(0, 0)

for i in l:
    if i > 30 * 500:
        r.append("N")
        continue
    if dp[n][i] == 1:
        r.append("Y")
    else:
        r.append("N")
print(*r)